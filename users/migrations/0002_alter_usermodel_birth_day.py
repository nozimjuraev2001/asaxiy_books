# Generated by Django 4.1.2 on 2022-10-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='birth_day',
            field=models.DateField(blank=True, null=True),
        ),
    ]