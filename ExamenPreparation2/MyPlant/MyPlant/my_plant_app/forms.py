from django import forms

from MyPlant.my_plant_app.models import ProfileModel, PlantModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['picture']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class PlantCreateForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'id': "id_description",
                }
            )
        }


class PlantDeleteForm(PlantCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
