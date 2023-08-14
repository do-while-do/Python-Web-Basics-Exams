from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from fruitipediaapp.web.validators import StartWithALetter


# Create your models here.
# •	Profile Model
# o	First Name
# 	Character field, required.
# 	It should consist of a maximum of 25 characters and a minimum of 2 characters.
# 	The first name must start with a letter. Otherwise raise ValidationError with the following message: "Your name must start with a letter!"
# o	Last Name
# 	Character field, required.
# 	It should consist of a maximum of 35 characters and a minimum of 1 character.
# 	The last name must start with a letter. Otherwise raise ValidationError with the following message: "Your name must start with a letter!"
# o	Email
# 	Email field, required.
# 	It should consist of a maximum of 40 characters.
# o	Password
# 	Character (password) field, required.
# 	It should consist of a maximum of 20 characters and a minimum of 8 characters.
# o	Image URL
# 	URL field, optional.
# o	Age
# 	Integer field, optional.
# 	The age default value should be 18.

class Profile(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(25),
            StartWithALetter('profile')
        ])
    last_name = models.CharField(
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(35),
            StartWithALetter('profile')
        ])
    email = models.EmailField(
        blank=False,
        null=False,
        validators=[
            MaxLengthValidator(40),
        ])
    password = models.CharField(
        validators=(MinLengthValidator(8), MaxLengthValidator(20)),
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=True,
        blank=True,
    )
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=18,
    )

    def __str__(self):
        return self.email


# •	Fruit Model
# o	Name
# 	Character field, required.
# 	It should consist of a maximum of 30 and a minimum of 2 characters.
# 	The name should contain only letters. Otherwise raise a ValidationError with the following message: "Fruit name should contain only letters!"
# o	Image URL
# 	URL field, required.
# o	Description
# 	Text field, required.
# o	Nutrition
# 	Text field, optional.
class Fruit(models.Model):
    fruit_name = models.CharField(
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(30),
            StartWithALetter('fruit')
        ]
    )
    image_url = models.URLField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    nutrition = models.TextField(blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.fruit_name
