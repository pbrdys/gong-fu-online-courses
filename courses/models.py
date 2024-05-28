from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

LEVEL = ((0, "Foundation"), (1, "Intermediate"), (2, "Advanced"))
CATEGORY = ((0, "Basics"), (1, "Qigong"), (2, "Taiji"), (3, "Bagua"), (4, "Taiyi"), (5, "Sword"), (6, "Gun"))

# Create your models here.
class Course(models.Model):
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
        ordering = ["level"]

class Lesson(models.Model):
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