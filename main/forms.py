from django import forms
from .models import MessageModel

class MessageModelForm(forms.ModelForm):

    class Meta:
        model = MessageModel
        exclude = ['created_at']
