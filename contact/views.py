from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def contact(request):
    
    if(request.method == "POST"):
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            
            messages.add_message(
                request, messages.SUCCESS,
                'Message successfully send.'
            )
            
    contact_form = ContactForm()
    
    return render(
        request,
        "contact.html",
        {
            "contact_form": contact_form, 
        },
    )