from .models import ContactFormModel
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormModel
        fields = ('name', 'email', 'subject', 'message')    