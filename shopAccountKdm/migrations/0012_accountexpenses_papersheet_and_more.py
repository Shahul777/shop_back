# Generated by Django 4.1.1 on 2022-09-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopAccountKdm', '0011_remove_accountexpenses_paperyesterday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountexpenses',
            name='PaperSheet',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='accountexpenses',
            name='PaperPresentToday',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='accountexpenses',
            name='PaperSoldToday',
            field=models.IntegerField(default=0),
        ),
    ]
