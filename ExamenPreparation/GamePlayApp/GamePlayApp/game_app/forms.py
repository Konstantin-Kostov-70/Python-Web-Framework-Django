from django import forms

from GamePlayApp.game_app.models import Profile, Game


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
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


