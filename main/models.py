from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from config.validators import PhoneValidator

class AboutModel(models.Model):
    image = models.ImageField(upload_to='about')
    body = RichTextUploadingField()

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'

class MessageModel(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(limit_value=4),
            MaxLengthValidator(limit_value=30)
            ])
    phone = models.CharField(max_length=13, validators=[PhoneValidator()])
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'