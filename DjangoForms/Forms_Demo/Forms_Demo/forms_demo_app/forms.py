from django import forms

from Forms_Demo.forms_demo_app.models import Student


class PersonForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your name',
                'class': 'input-fields',
            }
        )
    )
    age = forms.IntegerField()

    dev_level = forms.ChoiceField(
        choices=(
            ('junior', 'junior'),
            ('regular', 'regular'),
            ('senior', 'senior'),
        )
    )


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
