from django.db import models


# Create your models here.

class Recipe(models.Model):
    title = models.CharField(
        blank=False, null=False, max_length=30, unique=True
    )

    image_url = models.URLField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    ingredients = models.CharField(
        blank=False, null=False, max_length=250
    )
    time = models.IntegerField(blank=True, null=True)
