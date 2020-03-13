from django import forms
from .models import ConnectAccount
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class PayoutForm(forms.ModelForm):
    class Meta:
        model = ConnectAccount
        fields = ['first_name_kanji', 'first_name_kana', 'last_name_kanji', 'last_name_kana', 
        'gender', 'dob_day', 'dob_month', 'dob_year', 
        'post_code', 'kanji_state', 'kana_state', 'kanji_city', 'kana_city', 'kanji_town', 'kana_town', 
        'kanji_line1', 'kana_line1', 'kanji_line2', 'kana_line2', 'phone_number', 
        'account_number', 'bank_code', 'branch_code', 'account_holder_name']
        
        widgets = {
            'first_name_kanji': forms.TextInput(attrs={'placeholder': '記入例：太郎'},), 
            'first_name_kana': forms.TextInput(attrs={'placeholder': '記入例：タロウ'},), 
            'last_name_kanji': forms.TextInput(attrs={'placeholder': '記入例：田中'},), 
            'last_name_kana': forms.TextInput(attrs={'placeholder': '記入例：タナカ'},),

            'post_code': forms.TextInput(attrs={'class': 'p-postal-code','placeholder': '記入例：8900053',},),
            'kanji_state': forms.TextInput(attrs={'class': 'p-region','placeholder': '記入例：鹿児島県'},),
            'kana_state': forms.TextInput(attrs={'placeholder': '記入例：カゴシマケン'},),

            'kanji_city': forms.TextInput(attrs={'class': 'p-locality', 'placeholder': '記入例：鹿児島市'},),
            'kana_city': forms.TextInput(attrs={'placeholder': '記入例：カゴシマシ'},),

            'kanji_town': forms.TextInput(attrs={'class': 'p-street-address p-extended-address', 'placeholder': '記入例：中央町１丁目'},),
            'kana_town': forms.TextInput(attrs={'placeholder': '記入例：チュウオウチョウ１チョウメ'},),

            'kanji_line1': forms.TextInput(attrs={'class': 'p-extended-address', 'placeholder': '記入例：１０番２号 or １０−２'},),
            'kana_line1': forms.TextInput(attrs={'class': 'p-extended-address', 'placeholder': '記入例：１０バン２ゴウ or １０−２'},),
            'kanji_line2': forms.TextInput(attrs={'class': 'p-extended-address', 'placeholder': '記入例：アポロビル２０１号室'},),
            'kana_line2': forms.TextInput(attrs={'class': 'p-extended-address', 'placeholder': '記入例：アポロビル２０１ゴウシツ'},),

            'phone_number': forms.TextInput(attrs={'placeholder': '記入例：09012345678'},),
            'account_number': forms.TextInput(attrs={'placeholder': '記入例：0001234'},),
            'bank_code': forms.TextInput(attrs={'placeholder': '記入例：1100'},),
            'branch_code': forms.TextInput(attrs={'placeholder': '記入例：000'},),
            'account_holder_name': forms.TextInput(attrs={'placeholder': '記入例：タナカ タロウ'},),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field in self.fields.values():
        #     field.widget.attrs['class'] = 'form-control'
        #     field.widget.attrs['placeholder'] = ''

class AgreementForm(forms.ModelForm):
    class Meta:
        model = ConnectAccount
        fields = ['agreement']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
