from django import forms

from GamePlay.game_play_app.models import ProfileModel, Game


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }


class GameCreateForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class GameDeleteForm(GameCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
