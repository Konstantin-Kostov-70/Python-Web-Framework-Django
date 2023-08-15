from django.shortcuts import render, redirect

from MyPlant.my_plant_app.forms import ProfileCreateForm, PlantCreateForm, PlantDeleteForm, ProfileEditForm
from MyPlant.my_plant_app.models import ProfileModel, PlantModel


def get_profile():
    profile = ProfileModel.objects.first()
    return profile


def home(request):
    return render(request, 'home-page.html')


def catalog(request):
    all_plants = PlantModel.objects.all()
    context = {
        'all_plants': all_plants
    }
    return render(request, 'catalogue.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    context = {
        'form': form
    }
    return render(request, 'create-profile.html', context)


def profile_details(request):
    all_plants = PlantModel.objects.all()
    context = {
        'all_plants': all_plants,
    }
    return render(request, 'profile-details.html', context)


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
        'form': form
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    all_plants = PlantModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        all_plants.delete()
        return redirect('home')
    return render(request, 'delete-profile.html')


def plant_create(request):
    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    context = {
        'form': form
    }
    return render(request, 'create-plant.html', context)


def plant_details(request, pk):
    plant = PlantModel.objects.get(pk=pk)
    context = {
        'plant': plant
    }
    return render(request, 'plant-details.html', context)


def plant_edit(request, pk):
    plant = PlantModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = PlantCreateForm(instance=plant, initial=plant.__dict__)
    else:
        form = PlantCreateForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    context = {
        'form': form,
        'plant': plant
    }
    return render(request, 'edit-plant.html', context)


def plant_delete(request, pk):
    plant = PlantModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant, initial=plant.__dict__)
    else:
        plant.delete()
        return redirect('catalog')
    context = {
        'form': form,
        'plant': plant
    }
    return render(request, 'delete-plant.html', context)



