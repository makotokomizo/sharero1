# Generated by Django 3.0 on 2020-01-02 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0021_property_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='address',
            field=models.CharField(blank=True, max_length=40, verbose_name='市区町村番地'),
        ),
        migrations.AddField(
            model_name='property',
            name='bathesNumber',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='city',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='property',
            name='contextRoom',
            field=models.TextField(blank=True, help_text='何LDK，インテリア，近所にあるもの等', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='contextRule',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='contextStation',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='contextSurrounding',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='houseType',
            field=models.CharField(choices=[('マンション・アパート', 'apartment'), ('一軒家', 'isolated'), ('UR住宅', 'ur')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='maxMenber',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='meal',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='property',
            name='mealPrice',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='oneToOne',
            field=models.BooleanField(default=False, help_text='NESTER Designates whether the user can log into this admin site.'),
        ),
        migrations.AddField(
            model_name='property',
            name='owner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='ownerConfirm',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='property',
            name='postCode',
            field=models.CharField(blank=True, max_length=8, verbose_name='郵便番号'),
        ),
        migrations.AddField(
            model_name='property',
            name='prefecture',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='requirement1',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='property',
            name='requirement2',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='property',
            name='requirement3',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='property',
            name='requirement4',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='property',
            name='roomType',
            field=models.CharField(choices=[('部屋', 'simple'), ('離れ部屋', 'seperate')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='rule1',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='property',
            name='rule2',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='property',
            name='rule3',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='property',
            name='rule4',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='property',
            name='rule5',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='property',
            name='sharableItems',
            field=models.CharField(choices=[('Wi-Fi', 'wifi'), ('テレビ', 'tv'), ('電子レンジ', 'microwave'), ('エアコン', 'airconditioner'), ('机', 'desk'), ('ヘヤドライヤー', 'dryer')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='sharableSpace',
            field=models.CharField(choices=[('キッチン', 'kitchan'), ('洗濯機', 'washing'), ('洗濯乾燥機', 'drying'), ('駐車場', 'garage'), ('その他', 'other')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='span',
            field=models.CharField(choices=[('半年以下', 'short'), ('半年以上', 'long'), ('1年以上', 'verylong'), ('まだわからない', 'yet'), ('特定期間', 'special')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='startDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='toiletsNumber',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='beds_number',
            field=models.PositiveIntegerField(blank=True, default=2, null=True),
        ),
    ]
