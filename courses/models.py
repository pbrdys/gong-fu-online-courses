from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

LEVEL = ((0, "Foundation"), (1, "Intermediate"), (2, "Advanced"))
CATEGORY = (
    (0, "Basics"),
    (1, "Qigong"),
    (2, "Taiji"),
    (3, "Bagua"),
    (4, "Taiyi"),
    (5, "Sword"),
    (6, "Gun")
)


class Course(models.Model):
    """
    Model representing a course.

    Attributes:
        title (str): The title of the course.
        slug (str): The slug of the course.
        description (str): The description of the course.
        category (int): The category of the course.
        featured_image (CloudinaryField): The featured image of the course.
        content (str): The content of the course.
        level (int): The level of the course.
        created_on (datetime): The datetime when the course was created.
        updated_on (datetime): The datetime when the course was last updated.
        order (int): The order of the course.
    """

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    category = models.IntegerField(choices=CATEGORY, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    level = models.IntegerField(choices=LEVEL, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["order"]


class Lesson(models.Model):
    """
    Model representing a lesson.

    Attributes:
        course (Course): The course to which the lesson belongs.
        title (str): The title of the lesson.
        slug (str): The slug of the lesson.
        video_url (str): The URL of the video for the lesson.
        description (str): The description of the lesson.
        recommendation (str): Recommendations for the lesson.
        created_on (datetime): The datetime when the lesson was created.
        order (int): The order of the lesson.
    """

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lessons"
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    video_url = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    recommendation = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.course} - {self.title}"
    
    class Meta:
        ordering = ["order"]
