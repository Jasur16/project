# Generated by Django 4.0.6 on 2022-07-12 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_meaboutmodel_delete_aboutmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meaboutmodel',
            options={'verbose_name': 'about', 'verbose_name_plural': 'abouts'},
        ),
    ]
