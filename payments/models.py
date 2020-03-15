from django.db import models
from django.conf import settings
# from django.utils import timezone

# Create your models here.
# from register.models import User

class Plan(models.Model):
    title = models.CharField('タイトル', max_length=200)
    price = models.IntegerField(default=1000)
    description = models.TextField('説明', blank=True)
    plan_id = models.CharField('planID', max_length=200)
    # created_at = models.DateTimeField('日付', default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.title

class Transaction(models.Model):
    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, verbose_name='プラン', on_delete=models.PROTECT)
    token = models.CharField(max_length=120)
    order_id = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    success = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.order_id

    class Meta:
        ordering = ['-timestamp']

genderTYPE = (
    ("male", '男性'),
    ("female", '女性')
)
agreementYN = (
    (True, '同意します'),
    (False, '同意しません')
)


dayChoice = (
    ("1", '1'),
    ("2", '2'), 
    ("3", '3'),
    ("4", '4'), 
    ("5", '5'),
    ("6", '6'), 
    ("7", '7'),
    ("8", '8'), 
    ("9", '9'),
    ("10", '10'), 
    ("11", '11'),
    ("12", '12'), 
    ("13", '13'),
    ("14", '14'), 
    ("15", '15'),
    ("16", '16'), 
    ("17", '17'),
    ("18", '18'), 
    ("19", '19'),
    ("20", '20'), 
    ("21", '21'),
    ("22", '22'), 
    ("23", '23'),
    ("24", '24'), 
    ("25", '25'),
    ("26", '26'), 
    ("27", '27'),
    ("28", '28'), 
    ("29", '29'),
    ("30", '30'), 
    ("31", '31'), 
)

monthChoice = (
    ("1", '1'),
    ("2", '2'), 
    ("3", '3'),
    ("4", '4'), 
    ("5", '5'),
    ("6", '6'), 
    ("7", '7'),
    ("8", '8'), 
    ("9", '9'),
    ("10", '10'), 
    ("11", '11'),
    ("12", '12')
)

yearChoice = (
    ("1920", '1920'),
    ("1921", '1921'),
    ("1922", '1922'),
    ("1923", '1923'),
    ("1924", '1924'),
    ("1925", '1925'),
    ("1926", '1926'),
    ("1927", '1927'),
    ("1928", '1928'),
    ("1929", '1929'),
    ("1930", '1930'),
    ("1931", '1931'),
    ("1932", '1932'),
    ("1933", '1933'),
    ("1934", '1934'),
    ("1935", '1935'),
    ("1936", '1936'),
    ("1937", '1937'),
    ("1938", '1938'),
    ("1939", '1939'),
    ("1940", '1940'),
    ("1941", '1941'),
    ("1942", '1942'),
    ("1943", '1943'),
    ("1944", '1944'),
    ("1945", '1945'),
    ("1946", '1946'),
    ("1947", '1947'),
    ("1948", '1948'),
    ("1949", '1949'),
    ("1950", '1950'),
    ("1951", '1951'),
    ("1952", '1952'),
    ("1953", '1953'),
    ("1954", '1954'),
    ("1955", '1955'),
    ("1956", '1956'),
    ("1957", '1957'),
    ("1958", '1958'),
    ("1959", '1959'),
    ("1960", '1960'),
    ("1961", '1961'),
    ("1962", '1962'),
    ("1963", '1963'),
    ("1964", '1964'),
    ("1965", '1965'),
    ("1966", '1966'),
    ("1967", '1967'),
    ("1968", '1968'),
    ("1969", '1969'),
    ("1970", '1970'),
    ("1971", '1971'),
    ("1972", '1972'),
    ("1973", '1973'),
    ("1974", '1974'),
    ("1975", '1975'),
    ("1976", '1976'),
    ("1977", '1977'),
    ("1978", '1978'),
    ("1979", '1979'),
    ("1980", '1980'),
    ("1981", '1981'),
    ("1982", '1982'),
    ("1983", '1983'),
    ("1984", '1984'),
    ("1985", '1985'),
    ("1986", '1986'),
    ("1987", '1987'),
    ("1988", '1988'),
    ("1989", '1989'),
    ("1990", '1990'),
    ("2000", '2001'),
    ("2001", '2001'),
    ("2002", '2002'),
    ("2003", '2003'),
    ("2004", '2004'),
    ("2005", '2005'),
    ("2006", '2006'),
    ("2007", '2007'),
    ("2008", '2008'),
    ("2009", '2009'),
    ("2010", '2010'),
)

class ConnectAccount(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="connect_account", null=True, on_delete=models.SET_NULL)

    connect_id = models.CharField('connect_id', max_length=30)

    first_name_kanji = models.CharField('下の名前（漢字）', max_length=20)
    first_name_kana = models.CharField('下の名前（かな）', max_length=20)
    last_name_kanji = models.CharField('上の名前（漢字）', max_length=20)
    last_name_kana = models.CharField('上の名前（かな）', max_length=20)
    birth_date = models.DateTimeField('誕生日', null=True, blank=True)
    dob_day = models.CharField('誕生日（日）', max_length=2, choices=dayChoice, null=True)
    dob_month = models.CharField('誕生日（月）', max_length=2, choices=monthChoice, null=True)
    dob_year = models.CharField('誕生日（年）', max_length=4, choices=yearChoice, null=True)

    gender = models.CharField('性別', choices=genderTYPE, max_length=20)
    

    # address
    post_code = models.IntegerField('郵便番号', null=True)
    kana_state = models.CharField('都道府県（カナ）', max_length=20, null=True)
    kana_city = models.CharField('区市町村（カナ）', max_length=20, null=True)
    kana_town = models.CharField('町名（丁目まで、カナ）', max_length=20, null=True)
    kana_line1 = models.CharField('番地、号（カナ）', max_length=20, null=True)
    kana_line2 = models.CharField('建物・部屋番号・その他（カナ）', max_length=20, null=True, blank=True)

    kanji_state = models.CharField('都道府県（漢字）', max_length=20, null=True)
    kanji_city = models.CharField('区市町村（漢字）', max_length=20, null=True)
    kanji_town = models.CharField('町名（丁目まで、漢字）', max_length=20, null=True)
    kanji_line1 = models.CharField('番地、号（漢字）', max_length=20, null=True)
    kanji_line2 = models.CharField('建物・部屋番号・その他（漢字）', max_length=20, null=True, blank=True)

    email = models.EmailField('email address', unique=True, blank=True)
    phone_number = models.CharField('電話番号', unique=True, max_length=11, null=True)


    # bank
    object_account = models.CharField('タイプ', max_length=20, default='bank_account')
    account_number = models.CharField('口座番号(7桁)', max_length=7, null=True)
    bank_code = models.CharField('銀行コード(4桁)', max_length=4, null=True)
    branch_code = models.CharField('支店コード(3桁)', max_length=3, null=True)
    routing_number = models.CharField('routing_number', max_length=7, null=True) #銀行コード+支店コード
    account_holder_name = models.CharField('名義人', max_length=20, null=True)

    # agreement
    agreement = models.NullBooleanField('利用規約', choices=agreementYN)
    ip = models.GenericIPAddressField(null=True)
    acceptance_date = models.CharField('同意日', max_length=20, null=True)
    
    def __str__(self):
        return self.email


class Customer(models.Model):
    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer_id = models.CharField('CustumerID', max_length=200)
    email = models.EmailField('email address', unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.email



