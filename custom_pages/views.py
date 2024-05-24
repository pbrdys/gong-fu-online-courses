from django.shortcuts import render
from django.http import HttpResponseForbidden

# Custom permission check function
def user_has_permission(user):
    return user.is_superuser or user.is_authenticated


# access denied
def access_denied(request):
    response = render(request, 'access_denied.html')
    return HttpResponseForbidden(content=response.content, content_type='text/html')


# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)


def custom_500(request):
    raise Exception("Custom 500")