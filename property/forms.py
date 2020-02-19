from django import forms
from .models import Reserve, Property, SharableItem, SharableSpace, ExcludeMate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# User = get_user_model()

class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = '__all__'

class UserCreateForm(UserCreationForm):
    pass

class PropertyForm(forms.ModelForm):
    """家情報投稿フォーム"""

    class Meta:
        model = Property
        # fields = ['user', 'lastName', 'firstName', 'price', 'category', 'property_type', 'image', 'location', 'memo', 'birth_date']
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        # if lastName:
        #     self.fields['lastName'].widget.attrs['value'] = lastName
# class PropertySearch(forms.ModelForm):
#     class Meta:
#         model = Property
#         fields = ['address', 'property_type']

class PropertyForm2(forms.ModelForm):
    """家情報投稿フォーム"""
    # user = User
    # loca = user.email
    # print("form", loca)
    location = forms.CharField(help_text='必須項目です。')
    class Meta:
        model = User
        fields = ('email', 'location')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class Step1Form(forms.ModelForm):
    class Meta:
        model = Property
        # fields = ['lastName', 'firstName', 'maxMenber', 'roomType', 'prefecture', 'houseType', 'oneToOne', 'ownerConfirm']
        fields = ['petsType', 'furniture', 'member', 'memberUnder18', 'postCode', 'city', 'address']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class Step2Form(forms.ModelForm):
    class Meta:
        model = Property
        # fields = ['beds_number', 'toiletsNumber', 'bathesNumber']
        fields = ['title', 'contextSurrounding', 'contextRoom', 'contextStation', 'bathroomType', 'petsPermission', 'smokingPersiion', 'maxMenber', 'visiterPersiion', 'visiterStayPersiion', 'memoRoomDetail']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class Step3Form(forms.ModelForm):

    # sharableItems = forms.ModelMultipleChoiceField(
    #     queryset=SharableItem.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )
    class Meta:
        model = Property
        # fields = ['beds_number', 'toiletsNumber', 'bathesNumber']
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # if field != 'sharableItems':
            field.widget.attrs['class'] = 'form-control'

# class Step3Form(forms.ModelForm):
#     class Meta:
#         model = Property
#         # fields = ['beds_number', 'toiletsNumber', 'bathesNumber']
#         fields = ['beds_number', 'image', 'price', 'property_type', 'category', 'location']
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'
class ItemsRecordForm(forms.ModelForm):
    class Meta:
        model = Property
        # fields = ['beds_number', 'toiletsNumber', 'bathesNumber']
        fields = ['sharableItems']

class ItemsForm(forms.Form):
    sharableItemsList = (
        ("wifi", 'Wi-Fi'),
        ("tv", 'テレビ'),
        ("microwave", '電子レンジ'),
        ("airconditioner", 'エアコン'),
        ("heater", 'ヒーター'),
        ("gim", 'ジム'),
        ("dryer", 'ヘヤドライヤー'),
        ("other", '他')
    )
    sharableItems = forms.MultipleChoiceField(
        label='どんなアメニティが利用可能ですか？？',
        widget=forms.CheckboxSelectMultiple,
        choices=sharableItemsList,
        required=False,
    )

class SpaceForm(forms.Form):
    sharableSpaceList = (
        ("kitchan", 'キッチン'),
        ("garage", '駐車場'),
        ("living", 'リビング'),
        ("garden", '庭'),
        ("washar", '洗濯室'),
        ("toilet", 'トイレ'),
        ("other", '他')
    )
    sharableSpace = forms.MultipleChoiceField(
        label='どのスペースをメイトとシェアしますか？？',
        widget=forms.CheckboxSelectMultiple,
        choices=sharableSpaceList,
        required=False,
    )

class ExcludeForm(forms.Form):
    ExcludeList = (
        ("man", '男性'),
        ("woman", '女性'),
        ("student", '学生'),
        ("notStudent", '学生以外'),
        ("other", '他')
    )
    Exclude = forms.MultipleChoiceField(
        label='受け入れることが好ましくないタイプのメイトはいますか？？',
        widget=forms.CheckboxSelectMultiple,
        choices=ExcludeList,
        required=False,
    )
# class PropCreateForm(forms.ModelForm):
#     """ユーザー登録用フォーム"""

#     class Meta:
#         model = Property
#         fields = (User.USERNAME_FIELD,)  # ユーザー名として扱っているフィールドだけ、作成時に入力する

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'

class Step4Form(forms.ModelForm):
    class Meta:
        model = Property
        # fields = ['beds_number', 'toiletsNumber', 'bathesNumber']
        fields = ['price', 'includeAdditionalFee', 'addtionalPrice']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class Step5Form(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['lastName', 'firstName', 'age', 'gender', 'profile', 'collageName', 'facultyType', 'contextEducation', 'companyName', 'jobType', 'workingNow', 'contextJob', 'rootine', 'yourImage']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


