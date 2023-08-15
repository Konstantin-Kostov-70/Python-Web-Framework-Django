from django.shortcuts import render, redirect

from Car.car_app.forms import ProfileCreateForm, CarCreateForm, CarDeleteForm, ProfileEditForm
from Car.car_app.models import ProfileModel, CarModel


def get_profile():
    profile = ProfileModel.objects.first()
    return profile


def index(request):
    return render(request, 'index.html')


def catalog(request):
    all_cars = CarModel.objects.all()
    context = {
        'all_cars': all_cars
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
    return render(request, 'profile-create.html', context)


def profile_details(request):
    all_cars = CarModel.objects.all()
    total_price = sum([car.price for car in all_cars])
    context = {
        'total_price': total_price
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

    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()
    all_cars = CarModel.objects.all()
    if request.method == 'POST':
        all_cars.delete()
        profile.delete()
        return redirect('index')
    return render(request, 'profile-delete.html')


def car_create(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    context = {
        'form': form
    }
    return render(request, 'car-create.html', context)


def car_details(request, pk):
    car = CarModel.objects.get(pk=pk)
    context = {
        'car': car
    }
    return render(request, 'car-details.html', context)


def car_edit(request, pk):
    car = CarModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = CarCreateForm(instance=car, initial=car.__dict__)
    else:
        form = CarCreateForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    context = {
        'form': form,
        'car': car
    }
    return render(request, 'car-edit.html', context)


def car_delete(request, pk):
    car = CarModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = CarDeleteForm(instance=car, initial=car.__dict__)
    else:
        car.delete()
        return redirect('catalog')
    context = {
        'form': form,
        'car': car
    }
    return render(request, 'car-delete.html', context)
