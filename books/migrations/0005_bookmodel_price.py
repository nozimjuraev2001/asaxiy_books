# Generated by Django 4.1.2 on 2022-10-28 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_featuresmodel_cover_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]