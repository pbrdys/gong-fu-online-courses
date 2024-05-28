# tests.py
from django.test import TestCase
from django.urls import reverse
from courses.models import Course, Lesson
from courses.forms import CourseForm, LessonForm

class CourseFormTest(TestCase):
    # MOCK DATA 
    ####################################################################
    ####################################################################
    def setUp(self):
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
        
    # TEST CASES 
    ####################################################################
    ####################################################################
    
    # TEST FORM IS VALID
    def test_course_form_valid(self):
        form = CourseForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_course_form_invalid(self):
        form = CourseForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())

    # TEST ADDING COURSE
    def test_course_form_save(self):
        form = CourseForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
        course = form.save()
        self.assertEqual(course.title, 'Updated Test Course')
        self.assertEqual(Course.objects.count(), 2)

    # TEST UPDATE COURSE 
    def test_course_form_update(self):
        form = CourseForm(data=self.valid_data, instance=self.course)
        self.assertTrue(form.is_valid())
        updated_course = form.save()
        self.assertEqual(updated_course.title, 'Updated Test Course')
        self.assertEqual(updated_course.slug, 'updated-test-course')
        self.course.refresh_from_db()
        self.assertEqual(self.course.title, 'Updated Test Course')

    # TEST DELETE COURSE 
    def test_course_delete(self):
        self.course.delete()
        self.assertEqual(Course.objects.count(), 0)
    
    # TEST REQUIRED COURSE FIELDS
    def test_title_required(self):
        form_data = self.valid_data.copy()
        del form_data['title']
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_slug_required(self):
        form_data = self.valid_data.copy()
        del form_data['slug']
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('slug', form.errors)

    def test_description_required(self):
        form_data = self.valid_data.copy()
        del form_data['description']
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors)

    def test_category_required(self):
        form_data = self.valid_data.copy()
        del form_data['category']
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors)

    def test_content_required(self):
        form_data = self.valid_data.copy()
        del form_data['content']
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)

    def test_level_required(self):
        form_data = self.valid_data.copy()
        del form_data['level']
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('level', form.errors)

    def test_order_required(self):
        form_data = self.valid_data.copy()
        del form_data['order']
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('order', form.errors)

    # Invalid data tests
    # def test_invalid_title(self):
    #     form_data = self.valid_data.copy()
    #     form_data['title'] = 0  # Invalid data type
    #     form = CourseForm(data=form_data)
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('title', form.errors)
    
class LessonFormTest(TestCase):
    def setUp(self):
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
        form = LessonForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_lesson_form_invalid(self):
        form = LessonForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())

    def test_lesson_form_save(self):
        form = LessonForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
        lesson = form.save(commit=False)
        lesson.course = self.course
        lesson.save()
        self.assertEqual(lesson.title, 'Updated Test Lesson')
        self.assertEqual(Lesson.objects.count(), 2)  # Including the initial lesson

    def test_lesson_form_update(self):
        form = LessonForm(data=self.valid_data, instance=self.lesson)
        self.assertTrue(form.is_valid())
        updated_lesson = form.save()
        self.assertEqual(updated_lesson.title, 'Updated Test Lesson')
        self.assertEqual(updated_lesson.slug, 'updated-test-lesson')
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, 'Updated Test Lesson')

    def test_lesson_delete(self):
        self.lesson.delete()
        self.assertEqual(Lesson.objects.count(), 0)
        
    def test_title_required(self):
        form_data = self.valid_data.copy()
        del form_data['title']
        form = LessonForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_slug_required(self):
        form_data = self.valid_data.copy()
        del form_data['slug']
        form = LessonForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('slug', form.errors)

    def test_order_required(self):
        form_data = self.valid_data.copy()
        del form_data['order']
        form = LessonForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('order', form.errors)
