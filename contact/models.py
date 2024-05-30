from django.db import models


class ContactFormModel(models.Model):
    """
    Model representing a contact form submission.

    Attributes:
        name (str): The name of the person submitting the form.
        email (str): The email address of the person submitting the form.
        subject (str): The subject of the message.
        message (str): The content of the message.
        read (bool): Indicates whether the message has been read.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        """
        String representation of the contact form message.

        Returns:
            str: The name of the person who submitted the form.
        """
        return f"Contact Form Message - {self.name}"
