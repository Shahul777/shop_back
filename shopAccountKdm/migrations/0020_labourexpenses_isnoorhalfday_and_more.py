# Generated by Django 4.1.1 on 2022-09-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopAccountKdm', '0019_accountexpenses_paperquantitycame_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='labourexpenses',
            name='isNoorHalfDay',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='labourexpenses',
            name='isTajHalfDay',
            field=models.IntegerField(default=0),
        ),
    ]