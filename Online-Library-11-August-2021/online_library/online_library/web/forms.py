from django import forms

from online_library.web.models import Profile, Book


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name'
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'URL'
            })
        }
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "image_url": "Image URL",
        }


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = ['title', 'description', 'image_url']
        fields = '__all__'
        exclude = ['profile']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'title'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'description'
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'URL'
            }),
            'type': forms.TextInput(attrs={
                'placeholder': 'type'
            })
        }
        labels = {
            "title": "Title",
            "description": "Content",
            "image_url": "Image URL",
            "type": "Type",
        }


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }


class UserEditForm(UserBaseForm):
    pass


class UserDeleteForm(UserBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_readonly_fields()

    def __set_readonly_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
            field.required = False

    def save(self, commit=True):
        if commit:
            Book.objects.all().delete()
            self.instance.delete()
        return self.instance
