# Generated by Django 2.2.20 on 2021-11-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0007_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='arrival_time',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='train',
            name='departure_time',
            field=models.CharField(max_length=6),
        ),
    ]