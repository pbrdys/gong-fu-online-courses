from .models import ContactFormModel
from django import forms


class ContactForm(forms.ModelForm):
    """A form for contacting users."""

    class Meta:
        model = ContactFormModel
        fields = ('name', 'email', 'subject', 'message')
