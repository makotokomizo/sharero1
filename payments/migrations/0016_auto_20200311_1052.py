# Generated by Django 2.2 on 2020-03-11 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0015_auto_20200303_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectaccount',
            name='account_number',
            field=models.CharField(max_length=8, null=True, verbose_name='口座番号'),
        ),
        migrations.AlterField(
            model_name='connectaccount',
            name='bank_code',
            field=models.CharField(max_length=4, null=True, verbose_name='銀行コード'),
        ),
        migrations.AlterField(
            model_name='connectaccount',
            name='branch_code',
            field=models.CharField(max_length=3, null=True, verbose_name='支店コード'),
        ),
        migrations.AlterField(
            model_name='connectaccount',
            name='routing_number',
            field=models.CharField(max_length=7, null=True, verbose_name='routing_number'),
        ),
    ]
