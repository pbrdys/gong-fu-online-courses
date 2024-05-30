from django.shortcuts import render
from django.http import HttpResponseForbidden


def user_has_permission(user):
    """
    Checks if the user is a superuser or is authenticated.

    Args:
        user (User): The user to check for permission.

    Returns:
        bool: True if the user has permission, False otherwise.
    """
    return user.is_superuser or user.is_authenticated


def user_is_superuser(user):
    """
    Checks if the user is a superuser.

    Args:
        user (User): The user to check.

    Returns:
        bool: True if the user is a superuser, False otherwise.
    """
    return user.is_superuser


def access_denied(request):
    """
    Renders the access denied page.

    This function renders the 'access_denied.html' template and returns a
    HttpResponseForbidden response.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseForbidden
    """
    response = render(request, 'access_denied.html')
    return HttpResponseForbidden(
        content=response.content, content_type='text/html')


def custom_404(request, exception):
    """
    Renders the custom 404 page.

    This function renders the '404.html' template and returns a
    HttpResponseNotFound response with status code 404.

    Args:
        request (HttpRequest): The HTTP request object.
        exception: The exception that occurred (not used in this function).

    Returns:
        HttpResponseNotFound
    """
    return render(request, '404.html', status=404)


def custom_500(request):
    """
    Raises a custom 500 error.

    This function raises an Exception with the message "Custom 500".

    Args:
        request (HttpRequest): The HTTP request object

    Raises:
        Exception: Always raises an exception with the message "Custom 500".
    """
    raise Exception("Custom 500")
