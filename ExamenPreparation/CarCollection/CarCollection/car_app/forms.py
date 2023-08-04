from django import forms

from CarCollection.car_app.models import Profile, Car


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarDeleteForm(CarCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
