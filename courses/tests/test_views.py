from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from courses.models import Course, Lesson
from unittest.mock import patch
from django.contrib import messages
from courses.forms import CourseForm, LessonForm
from django.http import HttpResponseRedirect


class CourseViewsTests(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

        # Create a course
        self.course = Course.objects.create(
            title='Test Course',
            slug='test-course',
            description='Test Description',
            category=0,
            content='Test Course Content',
            level=0,
            order=1)

        # Create a lesson
        self.lesson = Lesson.objects.create(
            course=self.course,
            title='Test Lesson',
            slug='test-lesson',
            order=1)

        # URLs for the views
        self.course_detail_url = reverse(
            'course_detail', args=[self.course.slug])

        self.course_add_url = reverse('course_add')

        self.course_edit_url = reverse(
            'course_edit', args=[self.course.id])

        self.course_delete_url = reverse(
            'course_delete', args=[self.course.id])

        self.lesson_detail_url = reverse(
            'lesson_detail', args=[self.course.slug, self.lesson.slug])

        self.lesson_add_url = reverse(
            'lesson_add', args=[self.course.slug])

        self.lesson_edit_url = reverse(
            'lesson_edit', args=[self.course.slug, self.lesson.slug])

        self.lesson_delete_url = reverse(
            'lesson_delete', args=[self.course.slug, self.lesson.id])

        # Initialize the client
        self.client = Client()

    def login_user(self):
        self.client.login(username='testuser', password='testpassword')

    # Course Detail View Tests

    @patch('courses.views.user_has_permission', return_value=True)
    def test_course_detail_user_has_permission(self, mock_user_has_permission):
        self.login_user()
        response = self.client.get(self.course_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_detail.html')
        self.assertContains(response, self.course.title)
        self.assertContains(response, self.lesson.title)

    @patch('courses.views.user_has_permission', return_value=True)
    def test_course_detail_course_not_exist(self, mock_user_has_permission):
        self.login_user()
        non_existent_url = reverse('course_detail', args=['some-course'])
        response = self.client.get(non_existent_url)
        self.assertEqual(response.status_code, 404)

    @patch('courses.views.user_has_permission', return_value=False)
    def test_course_detail_user_no_permission(self, mock_user_has_permission):
        self.login_user()
        response = self.client.get(self.course_detail_url)
        self.assertEqual(response.status_code, 403)

    @patch('courses.views.user_has_permission', return_value=False)
    def test_course_detailuser_not_logged_in(self, mock_user_has_permission):
        response = self.client.get(self.course_detail_url)
        self.assertNotEqual(response.status_code, 200)

    # Course Add View Tests

    @patch('courses.views.user_is_superuser', return_value=True)
    def test_course_add_valid_form(self, mock_user_is_superuser):
        self.login_user()
        data = {
            'title': 'New Course',
            'slug': 'new-course',
            'description': 'New Course Description',
            'category': 0,
            'content': 'This is a new course.',
            'level': 0,
            'order': 1
        }
        response = self.client.post(self.course_add_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Course successfully added')
        self.assertTrue(Course.objects.filter(slug='new-course').exists())

    @patch('courses.views.user_is_superuser', return_value=True)
    def test_course_add_invalid_form(self, mock_user_is_superuser):
        self.login_user()
        data = {
            'title': '',
            'slug': 'new-course',
            'description': 'New Course Description',
            'category': 0,
            'content': 'This is a new course.',
            'level': 0,
            'order': 1
        }
        response = self.client.post(self.course_add_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Form not valid')

        self.assertFalse(Course.objects.filter(slug='new-course').exists())

    @patch('courses.views.user_is_superuser', return_value=False)
    def test_course_add_user_no_permission(self, mock_user_is_superuser):
        self.login_user()
        response = self.client.get(self.course_add_url)
        self.assertEqual(response.status_code, 403)

    @patch('courses.views.user_is_superuser', return_value=True)
    def test_course_add_get_request(self, mock_user_is_superuser):
        self.login_user()
        response = self.client.get(self.course_add_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_add.html')
        self.assertIsInstance(response.context['course_form'], CourseForm)

    # Course Edit View Tests

    @patch('courses.views.user_is_superuser', return_value=True)
    def test_course_edit_valid_form(self, mock_user_is_superuser):
        self.login_user()
        data = {
            'title': 'Updated Course',
            'slug': 'test-course',
            'description': 'Updated Description',
            'category': 0,
            'content': 'Updated Content',
            'level': 0,
            'order': 1
        }
        response = self.client.post(self.course_edit_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('course_overview'))
        self.course.refresh_from_db()
        self.assertEqual(self.course.title, 'Updated Course')
        self.assertEqual(self.course.description, 'Updated Description')

    @patch('courses.views.user_is_superuser', return_value=True)
    def test_course_edit_invalid_form(self, mock_user_is_superuser):
        self.login_user()
        data = {
            'title': '',
            'slug': 'test-course',
            'description': 'Updated Description',
            'category': 0,
            'content': 'Updated Content',
            'level': 0,
            'order': 1
        }
        response = self.client.post(self.course_edit_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Error updating course!')
        self.course.refresh_from_db()
        self.assertNotEqual(self.course.description, 'Updated Description')

    @patch('courses.views.user_is_superuser', return_value=False)
    def test_course_edit_user_no_permission(self, mock_user_is_superuser):
        self.login_user()
        response = self.client.get(self.course_edit_url)
        self.assertEqual(response.status_code, 403)

    @patch('courses.views.user_is_superuser', return_value=True)
    def test_course_edit_get_request(self, mock_user_is_superuser):
        self.login_user()
        response = self.client.get(self.course_edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_edit.html')
        self.assertIsInstance(response.context['course_edit_form'], CourseForm)
        self.assertEqual(response.context['course'], self.course)

    # Course Delete View Tests

    @patch('courses.views.user_is_superuser', return_value=True)
    def test_course_delete_user_is_superuser(self, mock_user_is_superuser):
        self.login_user()
        response = self.client.post(self.course_delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('course_overview'))
        self.assertFalse(Course.objects.filter(id=self.course.id).exists())

    @patch('courses.views.user_is_superuser', return_value=False)
    def test_course_delete_user_no_permission(self, mock_user_is_superuser):
        self.login_user()
        response = self.client.post(self.course_delete_url)
        self.assertEqual(response.status_code, 403)

    # Lesson Detail View Tests

    @patch('courses.views.user_has_permission', return_value=True)
    def test_lesson_detail_view(self, mock_user_has_permission):
        self.login_user()
        response = self.client.get(self.lesson_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lesson_detail.html')
        self.assertContains(response, self.lesson.title)

    # Lesson Add View Tests

    @patch('courses.views.user_is_superuser', return_value=True)
    def test_lesson_add_valid_form(self, mock_user_is_superuser):
        self.login_user()
        data = {
            'title': 'New Lesson',
            'slug': 'new-lesson',
            'order': 1
        }
        response = self.client.post(self.lesson_add_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'course_detail', args=[self.course.slug]))

        self.assertTrue(Lesson.objects.filter(slug='new-lesson').exists())

    @patch('courses.views.user_is_superuser', return_value=True)
    def test_lesson_add_invalid_form(self, mock_user_is_superuser):
        self.login_user()
        data = {
            'title': '',
            'slug': 'new-lesson',
            'order': 1
        }
        response = self.client.post(self.lesson_add_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        self.assertFalse(Lesson.objects.filter(slug='new-lesson').exists())

    @patch('courses.views.user_is_superuser', return_value=False)
    def test_lesson_add_user_no_permission(self, mock_user_is_superuser):
        self.login_user()
        response = self.client.get(self.lesson_add_url)
        self.assertEqual(response.status_code, 403)

    @patch('courses.views.user_is_superuser', return_value=True)
    def test_lesson_add_get_request(self, mock_user_is_superuser):
        self.login_user()
        response = self.client.get(self.lesson_add_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lesson_add.html')
        self.assertIsInstance(response.context['lesson_form'], LessonForm)

    # Lesson Edit View Tests

    @patch('courses.views.user_is_superuser', return_value=True)
    def test_lesson_edit_valid_form(self, mock_user_is_superuser):
        self.login_user()
        data = {
            'title': 'Updated Lesson',
            'slug': 'test-lesson',
            'order': 1
        }
        response = self.client.post(self.lesson_edit_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'lesson_detail', args=[self.course.slug, self.lesson.slug]))

        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, 'Updated Lesson')

    @patch('courses.views.user_is_superuser', return_value=True)
    def test_lesson_edit_invalid_form(self, mock_user_is_superuser):
        self.login_user()
        data = {
            'title': '',
            'slug': 'test-lesson',
            'order': 1
        }
        response = self.client.post(self.lesson_edit_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        self.lesson.refresh_from_db()
        self.assertNotEqual(self.lesson.title, 'Updated Lesson')

    @patch('courses.views.user_is_superuser', return_value=False)
    def test_lesson_edit_user_no_permission(self, mock_user_is_superuser):
        self.login_user()
        response = self.client.get(self.lesson_edit_url)
        self.assertEqual(response.status_code, 403)

    @patch('courses.views.user_is_superuser', return_value=True)
    def test_lesson_edit_get_request(self, mock_user_is_superuser):
        self.login_user()
        response = self.client.get(self.lesson_edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lesson_edit.html')
        self.assertIsInstance(response.context['lesson_form'], LessonForm)
        self.assertEqual(response.context['lesson'], self.lesson)

    # Lesson Delete View Tests

    @patch('courses.views.user_is_superuser', return_value=True)
    def test_lesson_delete_user_is_superuser(self, mock_user_is_superuser):
        self.login_user()
        response = self.client.post(self.lesson_delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'course_detail', args=[self.course.slug]))

        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())

    @patch('courses.views.user_is_superuser', return_value=False)
    def test_lesson_delete_user_no_permission(self, mock_user_is_superuser):
        self.login_user()
        response = self.client.post(self.lesson_delete_url)
        self.assertEqual(response.status_code, 403)
