# Generated by Django 2.2 on 2020-02-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_auto_20200225_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='plan_id',
            field=models.CharField(default=1, max_length=200, verbose_name='planID'),
            preserve_default=False,
        ),
    ]
