from django.db import models
from django.conf import settings
# Create your models here.

propertyTYPE = (
    ("sale", 'あなたのもの'),
    ("rent", '借家')
)

roomTYPE = (
    ("simple", '部屋'),
    ("seperate", '離れ部屋')
)

houseTYPE = (
    ("apartment", 'マンション・アパート'),
    ("isolated", '一軒家'),
    ("ur", 'UR住宅')
)

sharableItemsList = (
    ("wifi", 'Wi-Fi'),
    ("tv", 'テレビ'),
    ("microwave", '電子レンジ'),
    ("airconditioner", 'エアコン'),
    ("desk", '机'),
    ("dryer", 'ヘヤドライヤー')
)

sharableSpaceList = (
    ("kitchan", 'キッチン'),
    ("washing", '洗濯機'),
    ("drying", '洗濯乾燥機'),
    ("garage", '駐車場'),
    ("other", 'その他')
)

spanTYPE = (
    ("short", '半年以下'),
    ("long", '半年以上'),
    ("verylong", '1年以上'),
    ("yet", 'まだわからない'),
    ("special", '特定期間')
)

genderTYPE = (
    ("man", '男性'),
    ("woman", '女性')
)

YesNo =  (
    (True, 'はい'),
    (False, 'いいえ')
)

class SharableItem(models.Model):
    name = models.CharField('共有物', max_length=255)
    def __str__(self):
        return self.name

class SharableSpace(models.Model):
    name = models.CharField('共有スペース', max_length=255)
    def __str__(self):
        return self.name

class ExcludeMate(models.Model):
    name = models.CharField('共有スペース', max_length=255)
    def __str__(self):
        return self.name
        
class Property(models.Model):
    submitStage = models.PositiveIntegerField(default=0,null=True, blank=True)
    public = models.BooleanField(default=False)


    #Step1------------
    petsType = models.CharField('ペットはいますか？', null=True, blank=True, max_length=50)
    furniture = models.CharField('家具付きですか？', null=True, blank=True, max_length=50)
    member =  models.CharField('現在の居住者', null=True, blank=True, max_length=50)
    memberUnder18 = models.CharField('18歳未満', null=True, blank=True, max_length=50)
    postCode = models.CharField('郵便番号',max_length=8,blank=True)
    city = models.CharField('市区', max_length=10, blank=True)
    address = models.CharField('町村番地',max_length=40,blank=True)
    #Step1------------

    #Step2------------
    title = models.CharField('あなたのお家に、目に留まるようなタイトルをつけましょう！',max_length=35, null=True, blank=True, help_text=(
            'ホームシェア物件を探しているメイトが一番初めに見る見出しです。あなたのお家のユニークな点を35文字以内で書いてみましょう！'),
    )
    contextSurrounding = models.TextField('お家やその周辺状況に関して、あなたの気に入っているところを紹介してみましょう',max_length=20, null=True, blank=True)
    contextRoom = models.TextField('提供するお部屋を紹介してください',max_length=20, null=True, blank=True, help_text=(
            '何LDK，インテリア，近所にあるもの等'),
    )
    contextStation = models.TextField('周辺の公共交通機関を教えてください',max_length=20, null=True, blank=True)
    bathroomType = models.CharField('メイトのバスルームタイプ',max_length=40,blank=True)
    sharableItems = models.ManyToManyField(SharableItem, verbose_name='共有物',blank=True)
    sharableSpace = models.ManyToManyField(SharableSpace, verbose_name='共有スペース',blank=True)
    excludeMateType = models.ManyToManyField(ExcludeMate, verbose_name='好ましくないメイト',blank=True)
    petsPermission = models.NullBooleanField('ペットを許可しますか??', choices=YesNo)  
    smokingPersiion = models.NullBooleanField('喫煙を許可しますか??', choices=YesNo) 
    maxMenber = models.PositiveIntegerField('ホームシェア可能な最大人数を教えてください。', default=1, null=True, blank=True)
    visiterPersiion = models.NullBooleanField('メイトの友達の招待を許可しますか?', choices=YesNo) 
    visiterStayPersiion = models.NullBooleanField('メイトの友達の宿泊を許可しますか?', choices=YesNo) 
    memoRoomDetail = models.TextField('他に、特筆事項があれば、ご記入ください', max_length=50, null=True, blank=True)

    #Step2------------

    #Step3 image------------
    image = models.ImageField('お部屋の写真1(必須)',upload_to='property/', null=True)
    image2 = models.ImageField('お部屋の写真2',upload_to='property/', null=True, blank=True)
    image3 = models.ImageField('お部屋の写真3',upload_to='property/', null=True, blank=True)
    image4 = models.ImageField('お部屋の写真4',upload_to='property/', null=True, blank=True)
    image5 = models.ImageField('お部屋の写真5',upload_to='property/', null=True, blank=True)

    #Step3 image------------

    #Step4 price------------
    price = models.PositiveIntegerField('家賃', null=True, blank=True)
    includeAdditionalFee = models.NullBooleanField('公共料金は含まれていますか?', choices=YesNo) 
    addtionalPrice = models.PositiveIntegerField('いいえの場合、メイトはいくら払う必要がありますか?', null=True, blank=True)
    #Step4 price------------

    #Step5 about you------------
    lastName = models.CharField('姓*', null=True, max_length=50)
    firstName = models.CharField('名*', null=True, max_length=50)
    age = models.PositiveIntegerField('年齢を教えてください*', null=True)
    gender = models.CharField('性別を教えてください*', choices=genderTYPE, max_length=10,null=True)
    profile = models.TextField('自己紹介を書いてみましょう！200文字以内',max_length=200, null=True, blank=True)
    #education---
    collageName = models.CharField('学校名',max_length=40,blank=True)
    facultyType = models.CharField('学部、学科、専攻',max_length=40,blank=True)
    contextEducation = models.TextField('研究、学んだこと、課題活動',max_length=200, null=True, blank=True)
    #job---
    companyName = models.CharField('企業名',max_length=40,blank=True)
    jobType = models.CharField('職業',max_length=40,blank=True)
    workingNow = models.NullBooleanField('現在もお仕事されていますか??', choices=YesNo) 
    contextJob = models.TextField('どういうお仕事をされていましたか？？(されていますか？？)',max_length=200, null=True, blank=True)

    rootine = models.CharField('ルーティーン',max_length=40,blank=True)
    yourImage = models.ImageField(upload_to='property/', null=True, blank=True)
    #Step5 about you------------

    roomType = models.CharField('お部屋のタイプ*', choices=roomTYPE, max_length=10,null=True, blank=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL, blank=True)
    houseType =  models.CharField('お家の種類*', choices=houseTYPE, max_length=10, null=True, blank=True)
    # oneToOne = models.BooleanField(
    #         '定員1名に独立した1部屋を提供できますか？？', 
    #         choices=YesNo,
    #         default=False
    # )
    oneToOne = models.NullBooleanField('定員1名に独立した1部屋を提供できますか？？', choices=YesNo, blank=True)
    ownerConfirm = models.NullBooleanField('物件所有者は登録者様ですか？？', choices=YesNo, blank=True)    


    
    toiletsNumber = models.PositiveIntegerField('トイレの数を教えてください。', null=True, blank=True)
    bathesNumber = models.PositiveIntegerField('お風呂の数を教えてください。', null=True, blank=True)


    # prefecture = models.CharField(max_length=10, null=True)
    # postCode = models.CharField(verbose_name='郵便番号',max_length=8,blank=True)
    
    
    # sharableItems = models.CharField(choices=sharableItemsList, max_length=30,null=True)
    # sharableSpace = models.CharField(choices=sharableSpaceList, max_length=10,null=True)
    # sharableItems = models.CharField('ホームシェア可能な最大人数を教えてください。', max_length=30,null=True)
    
    beds_number = models.PositiveIntegerField(default=2,null=True, blank=True)
    

    

    # owner = models.BooleanField(default=False)
    



    
    
    



    # requirement1 = models.NullBooleanField()
    # requirement2 = models.NullBooleanField()
    # requirement3 = models.NullBooleanField()
    # requirement4 = models.NullBooleanField()

    # rule1 = models.NullBooleanField()
    # rule2 = models.NullBooleanField()
    # rule3 = models.NullBooleanField()
    # rule4 = models.NullBooleanField()
    # rule5 = models.NullBooleanField()
    # contextRule = models.TextField(max_length=20, null=True, blank=True)



    # startDate = models.DateField(null=True, blank=True)
    # span = models.CharField(choices=spanTYPE, max_length=10, null=True)
    # meal = models.NullBooleanField()
    # mealPrice = models.PositiveIntegerField(default=0, null=True)






    property_type = models.CharField(choices=propertyTYPE, max_length=10, blank=True)
    
    
    # area = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    
    # garages_number = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="property", null=True, on_delete=models.SET_NULL)

    

    #引用してくる
    # email = models.EmailField(null=True, blank=True)
    # gender = models.CharField(max_length=2, null=True, blank=True)
    # adress = models.CharField(max_length=20, null=True, blank=True)
    # phone = models.CharField(max_length=20, null=True, blank=True)
    # birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'




class Category(models.Model):
    category_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category/', null=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Reserve(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    notes = models.TextField()

    def __str__(self):
        return self.name

# class mealEx(models.Model):
#     name = models.CharField('食事', max_length=255)
#     parent = models.ForeignKey(meal, verbose_name='meal', on_delete=models.PROTECT)

#     def __str__(self):
#         return self.name