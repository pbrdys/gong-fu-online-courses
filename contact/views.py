from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    """
    Handle the contact form submission and rendering.

    If the request method is POST, validate and save the contact form.
    If the form is valid, save the form data and display a success message.
    If the form is not valid, render the form with errors.
    If the request method is not POST, display an empty contact form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response with the rendered contact form.
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Message successfully sent.'
            )
            # Create a new empty form instance to clear the form
            contact_form = ContactForm()
        else:
            return render(
                request,
                "contact.html",
                {
                    "contact_form": contact_form,
                },
            )
    else:
        contact_form = ContactForm()

    return render(
        request,
        "contact.html",
        {
            "contact_form": contact_form,
        },
    )
