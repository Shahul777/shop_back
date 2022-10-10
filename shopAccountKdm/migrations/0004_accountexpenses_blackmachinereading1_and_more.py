# Generated by Django 4.1.1 on 2022-09-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopAccountKdm', '0003_alter_accountexpenses_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountexpenses',
            name='BlackMachineReading1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accountexpenses',
            name='BlackMachineReading2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accountexpenses',
            name='ColourMachineReading1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accountexpenses',
            name='Day',
            field=models.CharField(default='MON', max_length=10),
        ),
        migrations.AddField(
            model_name='accountexpenses',
            name='isHoliday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='accountexpenses',
            name='isSunday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='labourexpenses',
            name='Day',
            field=models.CharField(default='MON', max_length=10),
        ),
        migrations.AlterField(
            model_name='accountexpenses',
            name='PaperPresentToday',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='accountexpenses',
            name='PaperSoldToday',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='accountexpenses',
            name='PaperYesterday',
            field=models.CharField(max_length=100),
        ),
    ]