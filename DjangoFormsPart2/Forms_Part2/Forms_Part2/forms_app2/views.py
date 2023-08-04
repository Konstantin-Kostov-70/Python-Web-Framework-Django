from django.shortcuts import render, redirect

from Forms_Part2.forms_app2.forms import ValidateForm, ValidateModelForm, PersonCreateForm
from Forms_Part2.forms_app2.models import Person


def validate_form_view(request):
    display_text = None
    if request.method == 'GET':
        form = ValidateForm()
    else:
        form = ValidateForm(request.POST)
        if form.is_valid():
            display_text = 'All is valid'
        else:
            display_text = 'Not valid'
    context = {
        'display_text': display_text,
        'form': form
    }
    return render(request, 'index.html', context)


def model_form_validate_view(request):
    text = None
    if request.method == 'GET':
        form = ValidateModelForm()
    else:
        form = ValidateModelForm(request.POST)
        if form.is_valid():
            text = 'All is valid'
            form.save()
        else:
            text = 'Not valid'
    context = {
        'form': form,
        'text': text
    }
    return render(request, 'model-form.html', context)


def create_person_view(request):
    if request.method == 'GET':
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list person')
    context = {
        'form': form
    }
    return render(request, 'person.html', context)


def list_person(request):
    all_persons = Person.objects.all()
    context = {
        'all_persons': all_persons
    }
    return render(request, 'list-person.html', context)
