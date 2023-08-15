from django import forms

from MusicApp.my_music_app.models import ProfileModel, Album


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class AlbumDeleteForm(AlbumCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True

