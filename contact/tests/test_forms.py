from django.test import TestCase
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import ContactFormModel


class ContactFormTests(TestCase):
    """
    Test suite for the contact form functionality.
    """

    def setUp(self):
        """
        Set up the test data and URL for the contact form tests.
        """
        self.valid_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'subject': 'Inquiry',
            'message': 'This is a test message.'
        }
        self.invalid_data = {
            'name': '',
            'email': 'invalid-email',
            'subject': '',
            'message': ''
        }
        self.url = reverse('contact')

    def test_contact_form_valid_data(self):
        """
        Test the contact form with valid data.
        Ensure that the form submission is successful,
        the success message is displayed, and the data is saved.
        """
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Message successfully sent.')
        self.assertTrue(ContactFormModel.objects.filter(
            email='john.doe@example.com').exists())

    def test_contact_form_invalid_data(self):
        """
        Test the contact form with invalid data.
        Ensure that the form displays the appropriate error messages
        and the data is not saved.
        """
        response = self.client.post(self.url, data=self.invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'contact_form', 'name',
                             'This field is required.')
        self.assertFormError(response, 'contact_form', 'email',
                             'Enter a valid email address.')
        self.assertFormError(response, 'contact_form', 'subject',
                             'This field is required.')
        self.assertFormError(response, 'contact_form', 'message',
                             'This field is required.')
        self.assertFalse(ContactFormModel.objects.filter(
            email='invalid-email').exists())

    def test_contact_form_initial_render(self):
        """
        Test the initial rendering of the contact form.
        Ensure that the form is displayed correctly with the appropriate template.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertIsInstance(response.context['contact_form'], ContactForm)
        self.assertContains(response, '<form', 1)
        self.assertContains(response, 'type="submit"', 1)
