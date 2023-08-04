from django.shortcuts import render, redirect

from FruitipediaApp.fruit_app.forms import ProfileCreateForm, FruitCreateForm, FruitDeleteForm, ProfileEditForm, \
    FruitEditForm
from FruitipediaApp.fruit_app.models import ProfileModel, FruitModel


def get_profile():
    profile = ProfileModel.objects.first()
    return profile


def index(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'index.html', context)


def dashboard(request):
    all_fruits = FruitModel.objects.all()
    context = {
        'all_fruits': all_fruits
    }
    return render(request, 'dashboard.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'create-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile, initial=profile.__dict__)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')
    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    all_fruits = FruitModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        all_fruits.delete()
        return redirect('index')
    return render(request, 'delete-profile.html')


def profile_details(request):
    count = FruitModel.objects.all().count()
    context = {
        'count': count
    }
    return render(request, 'details-profile.html', context)


def fruit_create(request):
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form
    }

    return render(request, 'create-fruit.html', context)


def fruit_details(request, pk):
    fruit = FruitModel.objects.get(pk=pk)
    context = {
        'fruit': fruit
    }
    return render(request, 'details-fruit.html', context)


def fruit_edit(request, pk):
    fruit = FruitModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = FruitEditForm(instance=fruit, initial=fruit.__dict__)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'fruit': fruit
    }

    return render(request, 'edit-fruit.html', context)


def fruit_delete(request, pk):
    fruit = FruitModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit, initial=fruit.__dict__)
    else:
        fruit.delete()
        return redirect('dashboard')
    context = {
        'fruit': fruit,
        'form': form
    }
    return render(request, 'delete-fruit.html', context)



