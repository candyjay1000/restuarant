# Generated by Django 4.1 on 2022-10-22 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='preferred_location',
            field=models.CharField(max_length=60),
        ),
    ]