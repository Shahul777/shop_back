# Generated by Django 4.1.1 on 2022-09-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopAccountKdm', '0004_accountexpenses_blackmachinereading1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountexpenses',
            old_name='StayingCopies',
            new_name='TodayStayingCopies',
        ),
        migrations.RenameField(
            model_name='accountexpenses',
            old_name='StayingMoney',
            new_name='TodayStayingMoney',
        ),
        migrations.AddField(
            model_name='accountexpenses',
            name='OldStayingCopies',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accountexpenses',
            name='OldStayingMoney',
            field=models.IntegerField(default=0),
        ),
    ]
