# Generated by Django 4.0.6 on 2022-07-11 21:43

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_messagemodel_message_alter_messagemodel_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='body_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='aboutmodel',
            name='body_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
