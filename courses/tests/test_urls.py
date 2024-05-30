from django.test import SimpleTestCase
from django.urls import reverse, resolve
from courses import views


class TestUrls(SimpleTestCase):

    def test_course_overview_url_resolves(self):
        url = reverse('course_overview')
        self.assertEqual(resolve(url).func.view_class, views.course_overview)

    def test_course_add_url_resolves(self):
        url = reverse('course_add')
        self.assertEqual(resolve(url).func, views.course_add)

    def test_course_edit_url_resolves(self):
        url = reverse('course_edit', args=[1])
        self.assertEqual(resolve(url).func, views.course_edit)

    def test_course_delete_url_resolves(self):
        url = reverse('course_delete', args=[1])
        self.assertEqual(resolve(url).func, views.course_delete)

    def test_course_detail_url_resolves(self):
        url = reverse('course_detail', args=['course-slug'])
        self.assertEqual(resolve(url).func, views.course_detail)

    def test_lesson_add_url_resolves(self):
        url = reverse('lesson_add', args=['course-slug'])
        self.assertEqual(resolve(url).func, views.lesson_add)

    def test_lesson_detail_url_resolves(self):
        url = reverse('lesson_detail', args=['course-slug', 'lesson-slug'])
        self.assertEqual(resolve(url).func, views.lesson_detail)

    def test_lesson_edit_url_resolves(self):
        url = reverse('lesson_edit', args=['course-slug', 'lesson-slug'])
        self.assertEqual(resolve(url).func, views.lesson_edit)

    def test_lesson_delete_url_resolves(self):
        url = reverse('lesson_delete', args=['course-slug', 1])
        self.assertEqual(resolve(url).func, views.lesson_delete)
