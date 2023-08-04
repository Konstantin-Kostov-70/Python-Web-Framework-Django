from django import forms

from NotesApp.notes_app.models import Profile, Note


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class NoteDeleteForm(NoteCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True



