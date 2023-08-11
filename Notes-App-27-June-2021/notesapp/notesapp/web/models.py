from django.core.validators import MaxLengthValidator
from django.db import models


# •	Profile
# o	first_name - Character field with max length of 20 characters
# o	last_name - Character field with max length of 20 characters
# o	age - Integer field
# o	image_url - URL field

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=20, validators=[
        MaxLengthValidator(20),
    ])
    last_name = models.CharField(blank=False, null=False, max_length=20, validators=[
        MaxLengthValidator(20)
    ])
    age = models.PositiveIntegerField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.first_name


# •	Note
# o	title - Character field with max length of 30 characters
# o	image_url - URL field
# o	content - Text field
class Note(models.Model):
    title = models.CharField(
        blank=False, null=False, max_length=30, unique=True
    )
    image_url = models.URLField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
