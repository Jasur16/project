# Generated by Django 4.0.6 on 2022-07-12 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_aboutmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutmodel',
            old_name='imgage',
            new_name='image',
        ),
    ]
