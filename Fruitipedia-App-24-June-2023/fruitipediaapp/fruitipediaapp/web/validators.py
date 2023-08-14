from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class StartWithALetter:
    def __init__(self, choice):
        self.choice = choice

    def __call__(self, value):
        if not value[0].isalpha():
            if self.choice == 'fruit':
                raise ValidationError("Fruit name should contain only letters!")
            else:
                raise ValidationError("Your name must start with a letter!")

    def __eq__(self, other):
        return True
