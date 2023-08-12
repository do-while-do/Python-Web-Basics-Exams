from django.core.validators import MaxLengthValidator
from django.db import models


# Create your models here.
# •	Profile
# o	first_name - Character field with max length of 30 characters
# o	last_name - Character field with max length of 30 characters
# o	image_url - URL field
class Profile(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=30, validators=[
        MaxLengthValidator(30),
    ])
    last_name = models.CharField(blank=False, null=False, max_length=30, validators=[
        MaxLengthValidator(30),
    ])
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.first_name


# •	Book
# o	title - Character field with max length of 30 characters
# o	description - Text field
# o	image - URL field
# o	type - Character field with max length of 30 characters
class Book(models.Model):
    title = models.CharField(
        blank=False, null=False, max_length=30, unique=True
    )
    description = models.TextField(blank=False, null=False)
    image_url = models.URLField(blank=False, null=False)
    type = models.CharField(
        blank=False, null=False, max_length=30
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
