from django import forms

from FruitipediaApp.fruit_app.models import ProfileModel, FruitModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                },
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password'
                }
            ),

        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'image', 'age']


class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        labels = {
            'name': '',
            'image': '',
            'description': '',
            'nutrition': ''
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',
                },
            ),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image Url'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description'
                }
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition info'
                }
            ),
        }


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'


class FruitDeleteForm(FruitEditForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
