from django.db import models


# Create your models here.
class ContactFormModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact Form Message - {self.name}"
