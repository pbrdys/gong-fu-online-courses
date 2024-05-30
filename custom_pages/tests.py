from django.test import TestCase
from django.contrib.auth.models import User
from django.test import RequestFactory
from . import views


class CustomViewsTestCase(TestCase):
    """
    Test case class for custom views.

    Methods:
        test_user_has_permission: Test the user_has_permission view function.
        test_access_denied_view: Test the access_denied view function.
        test_custom_404_view: Test the custom_404 view function.
        test_custom_500_view: Test the custom_500 view function.
    """

    def test_user_has_permission(self):
        """
        Test the user_has_permission view function.

        This function tests whether the user_has_permission view correctly
        determines if a user has permission.

        It first creates a superuser and an authenticated user. Then, it checks
        whether the view returns True for both types of users.

        Returns:
            None
        """
        # Test superuser
        superuser = User.objects.create_superuser(
            'admin', 'admin@example.com', 'admin')

        self.assertTrue(views.user_has_permission(superuser))

        # Test authenticated user
        authenticated_user = User.objects.create_user(
            'user', 'user@example.com', 'password')

        self.assertTrue(views.user_has_permission(authenticated_user))

    def test_access_denied_view(self):
        """
        Test the access_denied view function.

        This function tests whether the access_denied view correctly returns
        a 403 Forbidden status code for both anonymous and authenticated users.

        Returns:
            None
        """
        # Test with an anonymous user
        request = RequestFactory().get('/')
        response = views.access_denied(request)
        self.assertEqual(response.status_code, 403)

        # Test with an authenticated user
        request.user = User.objects.create_user(
            'user', 'user@example.com', 'password')

        response = views.access_denied(request)
        self.assertEqual(response.status_code, 403)

    def test_custom_404_view(self):
        """
        Test the custom_404 view function.

        This function tests whether the custom_404 view correctly returns
        a 404 Not Found status code.

        Returns:
            None
        """
        # Test with a request
        request = RequestFactory().get('/')
        response = views.custom_404(request, None)
        self.assertEqual(response.status_code, 404)

    def test_custom_500_view(self):
        """
        Test the custom_500 view function.

        This function tests whether the custom_500 view correctly raises
        an exception.

        Returns:
            None
        """
        # Test that the view raises an exception
        with self.assertRaises(Exception):
            request = RequestFactory().get('/')
            views.custom_500(request)
