# Generated by Django 4.1.1 on 2022-09-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopAccountTpm', '0014_alter_labourexpenses_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountexpenses',
            name='PaperQuantityCame',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accountexpenses',
            name='PaperQuantitySent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accountexpenses',
            name='TonerQuantityCame',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accountexpenses',
            name='TonerQuantitySent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accountexpenses',
            name='isPaperSent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accountexpenses',
            name='isTonerSent',
            field=models.IntegerField(default=0),
        ),
    ]
