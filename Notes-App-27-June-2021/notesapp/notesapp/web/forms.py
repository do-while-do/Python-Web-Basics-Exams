from django import forms

from notesapp.web.models import Profile, Note


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "age": "Age",
            "image_url": "Link to Profile Image",
        }


class NoteModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description', 'image_url']
        exclude = ['profile']

        labels = {
            "title": "Title",
            "image_url": "Image URL",
            "description": "Content",
        }


class DeleteNoteModelForm(NoteModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs = {
                'readonly': 'readonly'
            }
