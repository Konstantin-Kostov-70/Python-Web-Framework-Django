from django.shortcuts import render, redirect

from MusicApp.my_music_app.forms import ProfileCreateForm, AlbumCreateForm, AlbumDeleteForm
from MusicApp.my_music_app.models import ProfileModel, Album


def home(request):
    profile = ProfileModel.objects.first()
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums
    }
    if profile:
        return render(request, 'home-with-profile.html', context)
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context['form'] = form

    return render(request,  'home-no-profile.html', context)


def album_add(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album
    }
    return render(request, 'album-details.html', context)


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'GET':
        form = AlbumCreateForm(instance=album, initial=album.__dict__)
    else:
        form = AlbumCreateForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
        'album': album
    }
    return render(request, 'edit-album.html', context)


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album, initial=album.__dict__)
    else:
        album.delete()
        return redirect('home')
    context = {
        'form': form,
        'album': album
    }
    return render(request, 'delete-album.html', context)


def profile_details(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = ProfileModel.objects.first()
    all_albums = Album.objects.all()
    if request.method == 'POST':
        profile.delete()
        all_albums.delete()
        return redirect('home')
    return render(request, 'profile-delete.html')
