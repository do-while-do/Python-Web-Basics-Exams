from django import forms

from recipes.web.models import Recipe


class RecipeModelForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            "title": "Title",
            "image_url": "Image URL",
            "description": "Description",
            "ingredients": "Ingredients",
            "time": "Time (Minutes)"
        }


class DeleteRecipeModelForm(RecipeModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs = {
                'readonly': 'readonly'
            }
