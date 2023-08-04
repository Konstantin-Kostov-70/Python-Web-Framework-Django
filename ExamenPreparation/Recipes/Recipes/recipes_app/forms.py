from django import forms

from Recipes.recipes_app.models import Recipe


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeDeleteForm(RecipeCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
