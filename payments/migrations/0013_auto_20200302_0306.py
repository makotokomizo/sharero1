# Generated by Django 2.2 on 2020-03-02 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0012_auto_20200302_0245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connectaccount',
            name='address_kana',
        ),
        migrations.RemoveField(
            model_name='connectaccount',
            name='address_kanji',
        ),
        migrations.AddField(
            model_name='connectaccount',
            name='kana_city',
            field=models.CharField(max_length=20, null=True, verbose_name='区市町村（カナ）'),
        ),
        migrations.AddField(
            model_name='connectaccount',
            name='kana_line1',
            field=models.CharField(max_length=20, null=True, verbose_name='番地、号（カナ）'),
        ),
        migrations.AddField(
            model_name='connectaccount',
            name='kana_line2',
            field=models.CharField(max_length=20, null=True, verbose_name='建物・部屋番号・その他（カナ）'),
        ),
        migrations.AddField(
            model_name='connectaccount',
            name='kana_state',
            field=models.CharField(max_length=20, null=True, verbose_name='都道府県（カナ）'),
        ),
        migrations.AddField(
            model_name='connectaccount',
            name='kana_town',
            field=models.CharField(max_length=20, null=True, verbose_name='町名（丁目まで、カナ）'),
        ),
        migrations.AddField(
            model_name='connectaccount',
            name='kanji_city',
            field=models.CharField(max_length=20, null=True, verbose_name='区市町村（漢字）'),
        ),
        migrations.AddField(
            model_name='connectaccount',
            name='kanji_line1',
            field=models.CharField(max_length=20, null=True, verbose_name='番地、号（漢字）'),
        ),
        migrations.AddField(
            model_name='connectaccount',
            name='kanji_line2',
            field=models.CharField(max_length=20, null=True, verbose_name='建物・部屋番号・その他（漢字）'),
        ),
        migrations.AddField(
            model_name='connectaccount',
            name='kanji_state',
            field=models.CharField(max_length=20, null=True, verbose_name='都道府県（漢字）'),
        ),
        migrations.AddField(
            model_name='connectaccount',
            name='kanji_town',
            field=models.CharField(max_length=20, null=True, verbose_name='町名（丁目まで、漢字）'),
        ),
        migrations.AlterField(
            model_name='connectaccount',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='誕生日'),
        ),
    ]
