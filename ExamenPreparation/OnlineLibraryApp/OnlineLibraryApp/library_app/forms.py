from django import forms

from OnlineLibraryApp.library_app.models import Profile, Book


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age'
                }
            ),

        }


class ProfileDeleteForm(ProfileCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description'
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Type'
                }
            ),

        }


