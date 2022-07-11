from dataclasses import field
from modeltranslation.translator import register, TranslationOptions
from .models import AboutModel

@register(AboutModel)
class AboutModelTranslationOptions(TranslationOptions):
    fields = ['body']