# Generated by Django 3.0 on 2019-12-19 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20191219_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='adress',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='property',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='gender',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='property',
            name='memo',
            field=models.TextField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='property',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
