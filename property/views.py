from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from .models import Property, Category, SharableItem, SharableSpace, ExcludeMate
from .forms import (ReserveForm, PropertyForm, PropertyUpdateForm, UserCreateForm, 
Step1Form, Step2Form, Step3Form, Step4Form, Step5Form, ItemsForm, ItemsRecordForm, SpaceForm, ExcludeForm)
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
User = get_user_model()

def property_list(request):
    property_list = Property.objects.filter(public=True)
    template = 'property/list.html'
    # print(property_list(property_type="sale").query)
    # print(property_list.property_type)
    # address_query = request.GET.get('q')
    # property_type = request.GET.get('property_type', None)
    # if address_query and property_type:
    #     property_list = property_list.filter(
    #         Q(name__icontains = address_query) &
    #         Q(property_type__icontains = property_type[0])
    #     ).distinct()
    #     # print(search_query)
    #     # print(property_type)
    
    q_kwargs = {}
    # gender = property_list.get('gender')
    address_query = request.GET.get('q') #search info.
    property_type_query = request.GET.get('property_type', None) #search info.
    
    # result = Property.objects.values_list('property_type', flat=True).get(pk=1)
    # print('result = ' + result)
    # if gender:
    #     q_kwargs['gender'] = gender
    # if address_query and property_type:
    #     print("inin")
    #     property_list = property_list.filter(
    #         # Q(name__icontains = address_query) &
    #         Q(property_type__icontains = property_type)
    #         )

    # if address_query and property_type_query:
    #     property_list = property_list.filter(
    #         Q(property_type__icontains = property_type_query)     #1:rent 2:sale
    #         &
    #         Q(location__icontains = address_query)
    #         )

    if address_query and property_type_query:
        property_list = property_list.filter(
            Q(location__icontains = address_query)
            )

    context = {
        'property_list' : property_list
    }
    print(property_type_query)
    print(address_query)
    print(context)
    

    return render(request, template, context)

def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    template = 'property/detail.html'
    
    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()

    else:
        reserve_form = ReserveForm()
        
    context = {
        'property_detail' : property_detail,
        'reserve_form' : reserve_form
    }

    return render(request, template, context)

# def property_submit1(request):
#     template = 'property/submit1.html'
#     user_pk = request.user.pk
#     result = User.objects.values_list('email', flat=True).get(pk=user_pk)
#     # result = User.objects.get(request)
#     print('result = ' + result)

#     if request.method == 'POST':
#         # property_form = PropertyForm(request.POST, request.FILES)
#         property_form = Step1Form(request.POST, request.FILES)
#         # property_info = Property(email=User.email)
#         if property_form.is_valid():
#             prop = property_form.save(commit=False)
#             prop.user = request.user
#             prop.save()
            
#             print("now3")
#             return redirect('property:property_submit2')
#             # return render(request, template, context)
#         else:
#             print("無効なフォームです")
#             print(property_form.errors)

#     else:
#         property_form = Step1Form()
#         # property_form = PropertyForm()
        
#         print("now2")
#     print("now")
    
#     context = {
#         'property_form' : property_form
#     }

#     return render(request, template, context)

def property_submit(request):
    template = 'property/submit1.html'
    user_pk = request.user.pk
    result = User.objects.values_list('username', flat=True).get(pk=user_pk)
    # result = User.objects.get(request)
    print('result = ' + result)
    if request.method == 'POST':
        # property_form = PropertyForm(request.POST, request.FILES)
        property_form = PropertyForm(request.POST, request.FILES)
        # property_info = Property(email=User.email)
        if property_form.is_valid():
            prop = property_form.save(commit=False)
            print("now11")
            prop.user = request.user
            prop.submitStage += 1
            # print("now12")
            prop.save()
            
            print("prop.submitStage")
            return redirect('register:user_create_done')
        else:
            print("無効なフォームです")
            print(property_form.errors)

    else:
        property_form = PropertyForm()
        # property_form = PropertyForm()
        
        print("now2")
    print("now")
    
    context = {
        'property_form' : property_form
    }

    return render(request, template, context)

def property_submit1(request):
    template = 'property/submit1.html'
    user_pk = request.user.pk
    # result = User.objects.values_list('username', flat=True).get(pk=user_pk)
    
    # result1 = User.objects.values_list('property', flat=True).get(pk=user_pk)
    # user = User()
    user =  User.objects.get(pk=user_pk)
    print("submit1_user_", user)

    # user.save()
    # prop = Property(user=user)
   
    # prop = Property.objects.create()
    
    # prop.save()
    # prop = Property.objects.get(user=user)
    
    
    
    # print("prop", prop)
    # result = User.objects.get(request)
    # print('result = ' + result)
    # print('result = ' + result1)
    if request.method == 'POST':
        prop, created = Property.objects.get_or_create(user=user)
        # property_form = PropertyForm(request.POST, request.FILES)
        property_form = Step1Form(request.POST, request.FILES, instance=prop)
        # property_info = Property(email=User.email)
        if property_form.is_valid():
            # prop = property_form.save(commit=False)
            print("hu122")
            property_form.save()
            print("submit1_created", prop, created)
            # prop = property_form.save(commit=False)
            # prop = property_form.cleaned_data
            # Property.objects.create(**property_form.cleaned_data)

            print("now11")
            # prop.user = request.user
            prop.submitStage = 1
            # # print("now12")
            # prop.user = user_
            prop.save()
            # result1 = property_form.save(commit=False)
            # print("now11")
            
            # result1.submitStage += 1
            # # print("now12")
            # result1.save()
            
            return redirect('property:property_submit2')
            # return render(request, template, context)
        else:
            print("無効なフォームです")
            print(property_form.errors)
        #       # GETリクエスト（初期表示）時はDBに保存されているデータをFormに結びつける
        # form = MessageForm({'message': message.message})

    else:
        property_form = Step1Form()
        # property_form = PropertyForm()
        
        print("now2")
    print("now")
    
    context = {
        'property_form' : property_form
    }

    return render(request, template, context)

def property_submit2(request):
    template = 'property/submit2.html'
    user_pk = request.user.pk
    user =  User.objects.get(pk=user_pk)
    pro_id = request.user.property.id
    prop = Property.objects.get(id=pro_id)
    # print("submit2_prop", prop.submitStage)
    if request.method == 'POST':
        property_form = Step2Form(request.POST, request.FILES, instance=prop)
        item_form = ItemsForm(request.POST)
        space_form = SpaceForm(request.POST)
        exclude_form = ExcludeForm(request.POST)
        # print("property_form", property_form)
        # print("item_form", item_form)
        for itemdata in item_form:
            print("item_form", itemdata.value())
            print("item_form", type(itemdata))
        for spacedata in space_form:
            print("space_form", type(spacedata))
        for excludedata in exclude_form:
            print("exclude_form", type(excludedata))

        # print("item_form2", item_form.data.value())
        # print("prop.item_form", prop.sharableItem)
        if property_form.is_valid() and item_form.is_valid() and space_form.is_valid() and exclude_form.is_valid():
            property_form.save()
            prop.submitStage = 2
            for indata in itemdata.value():
                print("indata", type(indata))
                new, created = SharableItem.objects.get_or_create(name=indata)
                print("new", type(new))
                prop.sharableItems.add(new)
            for indata in spacedata.value():
                new, created = SharableSpace.objects.get_or_create(name=indata)
                prop.sharableSpace.add(new)
            for indata in excludedata.value():
                new, created = ExcludeMate.objects.get_or_create(name=indata)
                prop.excludeMateType.add(new)
            # prop.objects.create(
            #     sharableItems=item_form.cleaned_data['sharableItems']
            # )

            prop.save()
            print("item_form_clear")
            return redirect('property:property_submit3')
        else:
            print("無効なフォームです")
            print(property_form.errors)
            print(item_form.errors)
            print(space_form.errors)
            print(exclude_form.errors)

    else:
        property_form = Step2Form()
        item_form = ItemsForm()
        space_form = SpaceForm()
        exclude_form = ExcludeForm()

    context = {
        'property_form' : property_form,
        'item_form' : item_form,
        'space_form' : space_form,
        'exclude_form' : exclude_form
    }
    return render(request, template, context)

def property_submit3(request):
    template = 'property/submit3.html'
    user_pk = request.user.pk
    user =  User.objects.get(pk=user_pk)
    pro_id = request.user.property.id
    prop = Property.objects.get(id=pro_id)
    print("submit3_prop", prop.submitStage)
    if request.method == 'POST':
        property_form = Step3Form(request.POST, request.FILES, instance=prop)
        # sharableItems_form = ItemsForm(request.POST)
        if property_form.is_valid():
            property_form.save()
            # selected_items = sharableItems_form['sharableItems']
            # print("selected_items", selected_items)
            # Property.objects.create(sharableItems=','.join(selected_items))
            prop.submitStage = 3
            prop.save()
            return redirect('property:property_submit4')
        else:
            print("無効なフォームです")
            print(property_form.errors)
    else:
        property_form = Step3Form()
        # sharableItems_form = ItemsForm()
    context = {
        'property_form' : property_form
    }
    return render(request, template, context)
# def property_submit3(request):
#     template = 'property/submit2.html'
#     user_pk = request.user.pk
#     user =  User.objects.get(pk=user_pk)
#     pro_id = request.user.property.id
#     prop = Property.objects.get(id=pro_id)
#     print("submit3_prop", prop.submitStage)
#     if request.method == 'POST':
#         property_form = Step3Form(request.POST, request.FILES, instance=prop)
#         sharableItems_form = ItemsForm(request.POST)
#         if property_form.is_valid() and sharableItems_form.is_valid():
#             property_form.save()
#             prop.sharableItems = sharableItems_form
#             prop.sharableItems.save()
#             # selected_items = sharableItems_form['sharableItems']
#             # print("selected_items", selected_items)
#             # Property.objects.create(sharableItems=','.join(selected_items))

#             prop.submitStage = 3
#             # prop.save()
#             return redirect('property:property_submit3')
#         else:
#             print("無効なフォームです")
#             print(property_form.errors)
#     else:
#         property_form = Step3Form()
#         sharableItems_form = ItemsForm()
#     context = {
#         'property_form' : property_form,
#         'sharableItems_form' : sharableItems_form
#     }
#     return render(request, template, context)


def property_submit4(request):
    template = 'property/submit4.html'
    user_pk = request.user.pk
    user =  User.objects.get(pk=user_pk)
    pro_id = request.user.property.id
    prop = Property.objects.get(id=pro_id)
    print("submit3_prop", prop.submitStage)
    if request.method == 'POST':
        property_form = Step4Form(request.POST, request.FILES, instance=prop)
        # sharableItems_form = ItemsForm(request.POST)
        if property_form.is_valid():
            property_form.save()
            # selected_items = sharableItems_form['sharableItems']
            # print("selected_items", selected_items)
            # Property.objects.create(sharableItems=','.join(selected_items))
            prop.submitStage = 4
            prop.save()
            return redirect('property:property_submit5')
        else:
            print("無効なフォームです")
            print(property_form.errors)
    else:
        property_form = Step4Form()
        # sharableItems_form = ItemsForm()
    context = {
        'property_form' : property_form
    }
    return render(request, template, context)

def property_submit5(request):
    template = 'property/submit5.html'
    user_pk = request.user.pk
    user =  User.objects.get(pk=user_pk)
    pro_id = request.user.property.id
    prop = Property.objects.get(id=pro_id)
    print("submit3_prop", prop.submitStage)
    if request.method == 'POST':
        property_form = Step5Form(request.POST, request.FILES, instance=prop)
        # sharableItems_form = ItemsForm(request.POST)
        if property_form.is_valid():
            property_form.save()
            # selected_items = sharableItems_form['sharableItems']
            # print("selected_items", selected_items)
            # Property.objects.create(sharableItems=','.join(selected_items))
            prop.submitStage = 5
            prop.save()
            return redirect('property:property_end')
        else:
            print("無効なフォームです")
            print(property_form.errors)
    else:
        property_form = Step5Form()
        # sharableItems_form = ItemsForm()
    context = {
        'property_form' : property_form
    }
    return render(request, template, context)

def property_end(request):
    template = 'property/end.html'
    return render(request, template)
# class property_submit(generic.UpdateView):
#     form_class = PropertyForm
#     template = 'property/submit.html'
    
#     def get_success_url(self):
#         return
def property_submit_complete(request):
    template = 'property/property_submit_complete.html'
    return render(request, template)

def property_my_detail(request, pk):
    template = 'property/property_my_detail.html'
    return render(request, template)

# def property_edit(request):
#     model = User
#     # property_form = PropertyForm
#     form_class = PropertyForm
#     template = 'property/property_edit.html'
#     return render(request, template)
    # def get_success_url(self):
    #     return resolve_url('property:property_my_detail')


# class OnlyYouMixin(UserPassesTestMixin):
#     """本人か、スーパーユーザーだけユーザーページアクセスを許可する"""
#     raise_exception = True

#     def test_func(self):
#         user = self.request.user
#         return user.pk == self.kwargs['pk'] or user.is_superuser

# class property_edit(OnlyYouMixin, generic.UpdateView):
#     model = Property
#     form_class = PropertyForm
#     template_name = 'property/property_edit.html'

    # def get_success_url(self):
    #     return resolve_url('property:property_edit.html', pk=self.kwargs['pk'])

def property_edit(request, pk):
    user = User.objects.get(pk=pk)
    print("here", user.pk)
    print("here", user.email)
    print("here", user.property.property_type)
    template = 'property/property_edit.html'
    # form = PropertyForm(request.POST, request.FILES, instance=user)
    
    # if request.method == 'POST':
    #     print("here", user.pk)
        
    #     if form.is_valid():
    #         # user = form.save()
    #         # user.refresh_from_db()
    #         # image = request.FILES.get('image')
    #         # user.profile.image = image

    #         # user.save()
    #         return redirect('home')
    # # else:
    # #     form = ProfileForm(
    # #         initial={
    # #                         #    'username': request.user.username,
    # #                         #    'image': request.user.profile.image,
    # #                         #    'email': request.user.email,
    # #                        }
    
    if request.method == 'POST':
        property_form = PropertyForm(request.POST, request.FILES)
        if property_form.is_valid():
            prop = property_form.save(commit=False)
            prop.user = request.user
            prop.save()
            
            print("now3")
            return redirect('property:property_submit_complete')
            # return render(request, template, context)
        else:
            print("無効なフォームです")
            print(property_form.errors)

    else:
        property_form = PropertyForm()
        print("now2")
        print("now4", user.property.property_type)
    print("now")
    
    # request = 'property:property_submit_complete'
    context = {
        'property_form' : property_form
    }
    # def get_success_url(self):
    #     return resolve_url('register:user_detail', pk=self.kwargs['pk'])

    return render(request, template, context)

class PropUpdate(generic.UpdateView):
    model = Property
    form_class = PropertyUpdateForm
    template_name = 'property/property_edit_test.html'  # デフォルトユーザーを使う場合に備え、きちんとtemplate名を書く

    def get_success_url(self):
        return resolve_url('property:property_my_detail', pk=self.kwargs['pk'])


class PropertyList(generic.ListView):
    """ユーザーを一覧表示。"""
    # デフォルトUserだと、authアプリケーションのuser_list.htmlを探すため、明示的に指定する。
    template_name = 'register/property_list.html'
    model = Property