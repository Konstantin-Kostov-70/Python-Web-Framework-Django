from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from MyMusicApp.music_app.forms import ProfileForm, AlbumForm, DeleteForm
from MyMusicApp.music_app.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get()
    except ObjectDoesNotExist:
        return None


def home(request):
    profile = get_profile()
    albums = Album.objects.all()

    if profile is None:
        if request.method == 'GET':
            form = ProfileForm()
            context = {
                'form': form,
                'not_profile': True
            }
            return render(request, 'home-no-profile.html', context)

        else:
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
    context = {
        'albums': albums
    }
    return render(request, 'home-with-profile.html', context)


def album_add(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(request.POST)
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
        form = AlbumForm(instance=album, initial=album.__dict__)
    else:
        form = AlbumForm(request.POST, instance=album)
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
        form = DeleteForm(instance=album, initial=album.__dict__)
    else:
        album.delete()
        return redirect('home')

    context = {
        'album': album,
        'form': form
    }
    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    albums = Album.objects.all()
    context = {
        'profile': profile,
        'count': albums.count()
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = get_profile()
    albums = Album.objects.all()
    if request.method == 'POST':
        profile.delete()
        albums.delete()
        return redirect('home')
    return render(request, 'profile-delete.html')


