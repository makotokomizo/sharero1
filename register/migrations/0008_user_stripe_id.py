# Generated by Django 2.2 on 2020-02-25 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
