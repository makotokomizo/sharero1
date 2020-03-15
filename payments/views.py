from django.shortcuts import redirect, render, get_object_or_404
import stripe
from django.http import HttpResponse
from ipware import get_client_ip

from django.conf import settings
# from django.views.generic.base import TemplateView
from django.views import generic, View
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import ConnectAccount
from .forms import PayoutForm, AgreementForm
import time

User = get_user_model()


from .models import Plan, Transaction, Customer

stripe.api_key = settings.STRIPE_SECRET_KEY


class HomePageView(generic.TemplateView):
    template_name = 'payments/home.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        plan = Plan.objects.get(pk=1)
        print("plan", plan.price)
        context['amount'] = plan.price
        return context

class TestView(generic.TemplateView):
    template_name = 'payments/charge.html'

# @login_required()
# def check(request, pk):
#     plan = Plan.objects.get(pk=pk)
#     template = 'payments/home.html'
    
#     context = {
#         'key' : settings.STRIPE_PUBLISHABLE_KEY,
#         'amount' : plan.price
#     }

#     return render(request, template, context)

@login_required()
def check(request, token):
    print("PlanID", token)
    plan = Plan.objects.get(plan_id=token)
    template = 'payments/home.html'
    # print("PlanID2", pk)
    print("plan", plan.price)

    # if request.method == 'POST':
    #     reserve_form = ReserveForm(request.POST)
    #     if reserve_form.is_valid():
    #         reserve_form.save()

    # else:
    #     reserve_form = ReserveForm()
    
    context = {
        'key' : settings.STRIPE_PUBLISHABLE_KEY,
        'amount' : plan.price,
        'plan_id': plan.plan_id
    }

    return render(request, template, context)


# @login_required()
def charge(request, token): # new
    if request.method == 'POST':
        print("request.POST", request.POST)
        stripetoken = request.POST['stripeToken']
        plan = Plan.objects.get(plan_id=token)

        # connect_account = stripe.Account.retrieve("acct_1GIF7FBlqfggZIpQ")
        # print("connect_account", connect_account)
        try:
            # charge = stripe.Charge.create(
            #     amount=plan.price,
            #     currency='jpy',
            #     source=token,
            #     description='メール:{} 書籍名:{}'.format(request.user.email, plan.title),
            # )
            customer_DB, created = Customer.objects.get_or_create(profile=request.user, email=request.user.email)
            print("customer_created", created)



            # acct = stripe.Account.create(
            #     country="JP",
            #     type="custom",
            #     requested_capabilities=['card_payments', 'transfers'],
            #     business_type = "individual",
            #     email=request.user.email,
            #     )

            if not created:
                print("customer_created1")
                customer = stripe.Customer.retrieve(
                    customer_DB.customer_id
                    )
                print("customer_created2")

            else:
                print("customer_created3")
                customer = stripe.Customer.create(
                    email=request.user.email,
                    source=stripetoken,
                    # stripe_account=connect_account.id,
                    )
                # customer= stripe.Customer.retrieve()
                customer_DB.customer_id = customer.id
                customer_DB.save()
                print("customer_created4")

            token_connect = stripe.Token.create(
                customer=customer.id,
                stripe_account=connect_account.id,
                )
            print("token_created")

            customer = stripe.Customer.create(
                source=token_connect.id,
                stripe_account=connect_account.id,
                )
            print("customer", customer)

            subscription_plan = stripe.Plan.create(
                nickname="家賃"+str(plan.price)+"円",
                # id="monthly"+str(plan.price),
                interval="month",
                currency="jpy",
                amount=plan.price,
                product={"name": "ShareRo"},
                stripe_account=connect_account.id,
            )

            
            # subscription = stripe.Subscription.create(
            #     customer=customer,
            #     items=[{'plan': "plan_Gq8Jd3XSwvYNiw"}],
            #     application_fee_percent=10,
            #     stripe_account = "acct_1GIF7FBlqfggZIpQ"
            #     )

            # subscription = stripe.Subscription.create(
            #     customer=customer,
            #     items=[{'plan': subscription_plan.id}],
            #     )
            subscription = stripe.Subscription.create(
                customer=customer,
                items=[{'plan': subscription_plan.id}],
                application_fee_percent=10,
                stripe_account=connect_account.id
                )

        except stripe.error.CardError as e:
            # カード決済が上手く行かなかった(限度額超えとか)ので、メッセージと一緒に再度ページ表示
            context = self.get_context_data()
            context['message'] = 'Your payment cannot be completed. The card has been declined.'
            return render(request, 'payments/charge.html', context)
        else:
            # 上手く購入できた。Django側にも購入履歴を入れておく
            Transaction.objects.create(plan=plan, profile=request.user, token=stripetoken, 
            order_id=plan.id, amount=plan.price, success=True)

            return render(request, 'payments/charge.html')


# connect利用規約
@login_required
def agreement(request):
    template = 'payments/agreement.html'
    user_pk = request.user.pk
    user =  User.objects.get(pk=user_pk)
    if request.method == 'POST':
        print("user", user, user.email)

        prop, created = ConnectAccount.objects.get_or_create(email=user.email)
        print("prop", prop)

        agreement_form = AgreementForm(request.POST, instance=prop)
        print("agreement_form", agreement_form)
        if agreement_form.is_valid():
            agreement_form.save()
            print("submit1_created", prop, created)
            try:
                acct = stripe.Account.retrieve(prop)
            except:
                acct = stripe.Account.create(
                    country="JP",
                    type="custom",
                    requested_capabilities=['card_payments', 'transfers'],
                    business_type = "individual",
                    email=prop.email,
                    individual = {"first_name_kanji":"太郎"}
                    )


            print("ip", get_ip(request))
            print("date", int(time.time()))
            
            acct.tos_acceptance = {"date":int(time.time()), "ip" : get_ip(request)}
            acct.save()
            prop.user = user
            prop.connect_id = acct.id

            prop.ip = get_ip(request)
            prop.acceptance_date = int(time.time())
            prop.save()
            print("acct", acct)


            # prop.submitStage = 1
            # prop.save()
            
            return redirect('payments:connect_submit')
            # return render(request, template, context)
        else:
            print("無効なフォームです")
            print(agreement_form.errors)

    else:
        agreement_form = AgreementForm()
    
    context = {
        'agreement_form' : agreement_form
    }

    return render(request, template, context)
# connect利用規約


# コネクトアカウント作成
@login_required
def connect_submit(request):
    template = 'payments/submit.html'
    user_pk = request.user.pk
    user =  User.objects.get(pk=user_pk)

    if request.method == 'POST':
        print("user", user, user.email)

        prop, created = ConnectAccount.objects.get_or_create(email=user.email)
        print("prop", prop)

        payout_form = PayoutForm(request.POST, request.FILES, instance=prop)

        if payout_form.is_valid():
            payout_form.save()
            print("submit1_created", prop, created)
            try:
                acct = stripe.Account.retrieve(prop.connect_id)
            except:
                acct = stripe.Account.create(
                    country="JP",
                    type="custom",
                    requested_capabilities=['card_payments', 'transfers'],
                    business_type = "individual",
                    email=prop.email,
                    individual = {"first_name":prop.first_name_kanji}
                    )

            print("acct1", acct)

            prop.routing_number = str(prop.bank_code) + str(prop.branch_code)
            prop.save()


            acct.individual.last_name_kana = prop.last_name_kana
            print("here01")
            acct.individual.last_name_kanji = prop.last_name_kanji
            acct.individual.first_name_kana = prop.first_name_kana
            acct.individual.first_name_kanji = prop.first_name_kanji
            acct.individual.gender = prop.gender
            acct.individual.dob.day = prop.dob_day
            acct.individual.dob.month = prop.dob_month
            acct.individual.dob.year = prop.dob_year
            # acct.individual.phone_number = prop.phone_number

            # address info.
            acct.individual.address_kana.postal_code = prop.post_code
            acct.individual.address_kana.state = prop.kana_state
            acct.individual.address_kana.city = prop.kana_city
            acct.individual.address_kana.town = prop.kana_town
            acct.individual.address_kana.line1 = prop.kana_line1
            acct.individual.address_kana.line2 = prop.kana_line2
            print("acct3", acct)
            acct.save()
            acct.individual.address_kanji.postal_code = prop.post_code
            acct.individual.address_kanji.state = prop.kanji_state
            acct.individual.address_kanji.city = prop.kanji_city
            acct.individual.address_kanji.town = prop.kanji_town
            acct.individual.address_kanji.line1 = prop.kanji_line1
            acct.individual.address_kanji.line2 = prop.kanji_line2


            # # bank info.
            acct.external_accounts.create(external_account= {
                'object_account':prop.object_account,
                'account_number': prop.account_number,
                'routing_number': prop.routing_number, #銀行コード+支店コード
                'account_holder_name':prop.account_holder_name,
                'currency':'jpy',
                'country':'jp',
            })

            acct.save()
            
            return redirect('payments:charge_kari')
            # return render(request, template, context)
        else:
            print("無効なフォームです")
            print(payout_form.errors)

    else:
        payout_form = PayoutForm()
    
    context = {
        'payout_form' : payout_form
    }

    return render(request, template, context)
# コネクトアカウント作成



# def connect(request):
#     acct = stripe.Account.create(
#         country="JP",
#         type="custom",
#         requested_capabilities=['card_payments', 'transfers'],
#         )
#     print("acct", acct)

#     return render(request, 'payments/charge.html')


# ipアドレス取得テスト
class MyView(View):
    def get(self, request):
        client_addr, _ = get_client_ip(request)

        return HttpResponse(client_addr)

def get_ip(request):
        client_addr, _ = get_client_ip(request)

        return client_addr