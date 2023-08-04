from django import forms

from MyMusicApp.music_app.models import Profile, Album


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'username'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'type': 'number',
                    'placeholder': 'Age',
                }
            ),
        }


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name'
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'type': 'number',
                    'placeholder': 'Price',
                }
            ),
        }


class DeleteForm(AlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
