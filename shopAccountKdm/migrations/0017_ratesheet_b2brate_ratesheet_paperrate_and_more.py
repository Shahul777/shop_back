# Generated by Django 4.1.1 on 2022-09-19 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopAccountKdm', '0016_accountexpenses_colourmachinereading2'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratesheet',
            name='b2bRate',
            field=models.DecimalField(decimal_places=2, default=0.85, max_digits=9),
        ),
        migrations.AddField(
            model_name='ratesheet',
            name='paperRate',
            field=models.DecimalField(decimal_places=2, default=0.5, max_digits=9),
        ),
        migrations.AddField(
            model_name='ratesheet',
            name='singleRate',
            field=models.DecimalField(decimal_places=2, default=1.25, max_digits=9),
        ),
        migrations.AddField(
            model_name='ratesheet',
            name='tonerRate',
            field=models.DecimalField(decimal_places=2, default=800.0, max_digits=9),
        ),
    ]
