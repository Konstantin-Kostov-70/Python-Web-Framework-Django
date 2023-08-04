from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from NotesApp.notes_app.forms import ProfileCreateForm, NoteCreateForm, NoteDeleteForm
from NotesApp.notes_app.models import Profile, Note


def get_profile():
    try:
        return Profile.objects.get()
    except ObjectDoesNotExist:
        return None


def index(request):
    profile = get_profile()
    all_notes = Note.objects.all()
    if profile is None:
        if request.method == 'GET':
            form = ProfileCreateForm()
            context = {
                'form': form,
                'not_profile': True,
            }
            return render(request, 'home-no-profile.html', context)
        else:
            form = ProfileCreateForm(request.POST)
            if form.is_valid():
                form.save()
    context = {
        'all_notes': all_notes
    }
    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'GET':
        form = NoteCreateForm()
    else:
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        form = NoteCreateForm(instance=note, initial=note.__dict__)
    else:
        form = NoteCreateForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'note': note
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        form = NoteDeleteForm(instance=note, initial=note.__dict__)
    else:
        note.delete()
        return redirect('index')
    context = {
        'form': form,
        'note': note
    }
    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)


def profile(request):
    count = Note.objects.all().count()
    profile = get_profile()
    context = {
        'profile': profile,
        'count': count
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    all_notes = note = Note.objects.all()

    profile.delete()
    all_notes.delete()
    return redirect('index')
