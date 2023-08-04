from django import forms
from django.core.exceptions import ValidationError

from Forms_Part2.forms_app2.models import Todo, Person
from Forms_Part2.forms_app2.validators import validate_text, validate_priority, ValidateInRange


class ValidateForm(forms.Form):
    text = forms.CharField(
        validators=(
            validate_text,
        ),
    )
    is_done = forms.BooleanField(
        required=False
    )
    priority = forms.IntegerField(
        validators=(
            validate_priority,
        ),
    )
    level = forms.IntegerField(
        validators=(
            ValidateInRange(1, 20),
        )
    )


class ValidateModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

    def clean_assignee(self):
        assignee = self.cleaned_data['assignee']
        print(assignee.todo_set.count() )
        if assignee.todo_set.count() > Todo.MAX_TODOS_PER_PERSON:
            raise ValidationError('Assignee have max count of todos')
        return assignee

    # clean method must return value everything !!!!!!


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
