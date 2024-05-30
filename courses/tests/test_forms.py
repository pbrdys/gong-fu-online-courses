# tests.py
from django.test import TestCase
from courses.models import Course, Lesson
from courses.forms import CourseForm, LessonForm


class CourseFormTest(TestCase):
    """
    Test cases for the CourseForm.
    """

    def setUp(self):
        """
        Set up mock data for testing CourseForm.
        """
        self.course = Course.objects.create(
            title="Test Course",
            slug="test-course",
            description="Test Description",
            category=0,
            content="Test Course Content",
            level=0,
            order=0,
        )
        self.valid_data = {
            'title': 'Updated Test Course',
            'slug': 'updated-test-course',
            'description': 'Updated Test Description',
            'category': 0,
            'featured_image': None,  # Assuming this is optional
            'content': 'Updated Test Course Content',
            'level': 0,
            'order': 0,
        }
        self.invalid_data = {
            'title': '',  # Title is required
            'slug': 'updated-test-course',
            'description': 'Updated Test Description',
            'category': 0,
            'featured_image': None,
            'content': 'Updated Test Course Content',
            'level': 0,
            'order': 0,
        }

    def test_course_form_valid(self):
        """
        Test if the CourseForm is valid with valid data.
        """
        form = CourseForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_course_form_invalid(self):
        """
        Test if the CourseForm is invalid with invalid data.
        """
        form = CourseForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())

    def test_course_form_save(self):
        """
        Test if CourseForm saves correctly with valid data.
        """
        form = CourseForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
        course = form.save()
        self.assertEqual(course.title, 'Updated Test Course')
        self.assertEqual(Course.objects.count(), 2)

    def test_course_form_update(self):
        """
        Test if CourseForm updates correctly with valid data.
        """
        form = CourseForm(data=self.valid_data, instance=self.course)
        self.assertTrue(form.is_valid())
        updated_course = form.save()
        self.assertEqual(updated_course.title, 'Updated Test Course')
        self.assertEqual(updated_course.slug, 'updated-test-course')
        self.course.refresh_from_db()
        self.assertEqual(self.course.title, 'Updated Test Course')

    def test_course_delete(self):
        """
        Test if Course is deleted successfully.
        """
        self.course.delete()
        self.assertEqual(Course.objects.count(), 0)

    def test_title_required(self):
        """
        Test if the title field is required.
        """
        form_data = self.valid_data.copy()
        del form_data['title']
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_slug_required(self):
        """
        Test if the slug field is required.
        """
        form_data = self.valid_data.copy()
        del form_data['slug']
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('slug', form.errors)

    def test_description_required(self):
        """
        Test if the description field is required.
        """
        form_data = self.valid_data.copy()
        del form_data['description']
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors)

    def test_category_required(self):
        """
        Test if the category field is required.
        """
        form_data = self.valid_data.copy()
        del form_data['category']
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors)

    def test_content_required(self):
        """
        Test if the content field is required.
        """
        form_data = self.valid_data.copy()
        del form_data['content']
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)

    def test_level_required(self):
        """
        Test if the level field is required.
        """
        form_data = self.valid_data.copy()
        del form_data['level']
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('level', form.errors)

    def test_order_required(self):
        """
        Test if the order field is required.
        """
        form_data = self.valid_data.copy()
        del form_data['order']
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('order', form.errors)


class LessonFormTest(TestCase):
    """
    Test cases for the LessonForm.
    """

    def setUp(self):
        """
        Set up mock data for testing LessonForm.
        """
        self.course = Course.objects.create(
            title="Test Course",
            slug="test-course",
            description="Test Description",
            category=0,
            content="Test Course Content",
            level=0,
            order=0,
        )
        self.lesson = Lesson.objects.create(
            course=self.course,
            title="Test Lesson",
            slug="test-lesson",
            order=0,
        )
        self.valid_data = {
            'title': 'Updated Test Lesson',
            'slug': 'updated-test-lesson',
            'order': 0,
        }
        self.invalid_data = {
            'title': '',  # Title is required
            'slug': 'updated-test-lesson',
            'order': 0,
        }

    def test_lesson_form_valid(self):
        """
        Test if the LessonForm is valid with valid data.
        """
        form = LessonForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_lesson_form_invalid(self):
        """
        Test if the LessonForm is invalid with invalid data.
        """
        form = LessonForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())

    def test_lesson_form_save(self):
        """
        Test if LessonForm saves correctly with valid data.
        """
        form = LessonForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
        lesson = form.save(commit=False)
        lesson.course = self.course
        lesson.save()
        self.assertEqual(lesson.title, 'Updated Test Lesson')
        self.assertEqual(Lesson.objects.count(), 2)

    def test_lesson_form_update(self):
        """
        Test if LessonForm updates correctly with valid data.
        """
        form = LessonForm(data=self.valid_data, instance=self.lesson)
        self.assertTrue(form.is_valid())
        updated_lesson = form.save()
        self.assertEqual(updated_lesson.title, 'Updated Test Lesson')
        self.assertEqual(updated_lesson.slug, 'updated-test-lesson')
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, 'Updated Test Lesson')

    def test_lesson_delete(self):
        """
        Test if Lesson is deleted successfully.
        """
        self.lesson.delete()
        self.assertEqual(Lesson.objects.count(), 0)

    def test_title_required(self):
        """
        Test if the title field is required.
        """
        form_data = self.valid_data.copy()
        del form_data['title']
        form = LessonForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_slug_required(self):
        """
        Test if the slug field is required.
        """
        form_data = self.valid_data.copy()
        del form_data['slug']
        form = LessonForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('slug', form.errors)

    def test_order_required(self):
        """
        Test if the order field is required.
        """
        form_data = self.valid_data.copy()
        del form_data['order']
        form = LessonForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('order', form.errors)
