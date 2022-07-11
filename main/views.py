from django.shortcuts import redirect, render, reverse
from django.views.generic import TemplateView, ListView, CreateView
from .models import AboutModel, MessageModel
from .forms import MessageModelForm
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER
from .utils import send_bot_message


class HomeView(TemplateView):
    template_name = 'main/index.html'
    
    
class AboutView(ListView):
    model = AboutModel
    template_name = 'main/index.html'
    object_list = 'abouts'

class ContactView(CreateView):
    
    model = MessageModel
    form_class = MessageModelForm
    template_name = 'main/index.html'

    def get_success_url(self):
        return reverse('home')

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        # message = f"Salom {form.instance.name} ! Habaringiz qabul qilindi."
        # send_mail("Test", message, EMAIL_HOST_USER, [form.instance.email])
        send_bot_message(form.cleaned_data)
        return super().form_valid(form)