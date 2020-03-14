# Generated by Django 2.2 on 2020-03-11 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0017_auto_20200311_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectaccount',
            name='acceptance_date',
            field=models.CharField(max_length=20, null=True, verbose_name='同意日'),
        ),
        migrations.AddField(
            model_name='connectaccount',
            name='agreement',
            field=models.NullBooleanField(choices=[(True, '同意します'), (False, '同意しません')], verbose_name='利用規約'),
        ),
        migrations.AddField(
            model_name='connectaccount',
            name='ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='connectaccount',
            name='gender',
            field=models.CharField(choices=[('male', '男性'), ('female', '女性')], max_length=20, verbose_name='性別'),
        ),
    ]