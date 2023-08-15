from django import forms

from Car.car_app.models import ProfileModel, CarModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['username', 'email', 'age', 'password']
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


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarDeleteForm(CarCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
