from django import forms

from Frutipedia.fruit_app.models import ProfileModel, FruitModel


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
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
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
            )
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['password', 'email']


class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        labels = {
            'name': '',
            'image': '',
            'description': '',
            'nutrition': '',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name'
                }
            ),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description'
                }
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info'
                }
            )
        }


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        labels = {
            'name': 'Name:',
            'image': 'Image URL:',
            'description': 'Description:',
            'nutrition': 'Nutrition',
        }


class FruitDeleteForm(FruitEditForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nutrition'].widget.attrs['style'] = 'display: none;'
        self.fields['nutrition'].label = ''

        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True


