from django.shortcuts import render

# Custom permission check function
def user_has_permission(user):
    return user.is_superuser or user.is_authenticated


# access denied
def access_denied(request):
    return render(request, 'access_denied.html')


# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)


def custom_500(request):
    raise Exception("Custom 500")