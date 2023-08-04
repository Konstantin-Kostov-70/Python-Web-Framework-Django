from django import forms

from MyPlantApp.plant_app.models import ProfileModel, PlantModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class PlantCreateForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'


class PlantDeleteForm(PlantCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
