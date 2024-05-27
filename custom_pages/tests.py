from django.test import TestCase
from django.contrib.auth.models import User
from django.test import RequestFactory
from . import views

class CustomViewsTestCase(TestCase):

    def test_user_has_permission(self):
        # Test superuser
        superuser = User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        self.assertTrue(views.user_has_permission(superuser))

        # Test authenticated user
        authenticated_user = User.objects.create_user('user', 'user@example.com', 'password')
        self.assertTrue(views.user_has_permission(authenticated_user))

    def test_access_denied_view(self):
        # Test with an anonymous user
        request = RequestFactory().get('/')
        response = views.access_denied(request)
        self.assertEqual(response.status_code, 403)

        # Test with an authenticated user
        request.user = User.objects.create_user('user', 'user@example.com', 'password')
        response = views.access_denied(request)
        self.assertEqual(response.status_code, 403)

    def test_custom_404_view(self):
        # Test with a request
        request = RequestFactory().get('/')
        response = views.custom_404(request, None)
        self.assertEqual(response.status_code, 404)

    def test_custom_500_view(self):
        # Test that the view raises an exception
        with self.assertRaises(Exception):
            request = RequestFactory().get('/')
            views.custom_500(request)
