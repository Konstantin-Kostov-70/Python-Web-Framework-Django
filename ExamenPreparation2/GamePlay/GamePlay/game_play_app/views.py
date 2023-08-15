from django.shortcuts import render, redirect

from GamePlay.game_play_app.forms import ProfileCreateForm, GameCreateForm, GameDeleteForm, ProfileEditForm
from GamePlay.game_play_app.models import ProfileModel, Game


def get_profile():
    profile = ProfileModel.objects.first()
    return profile


def home(request):
    return render(request, 'home-page.html')


def dashboard(request):
    all_games = Game.objects.all()
    context = {
        'all_games': all_games
    }
    return render(request, 'dashboard.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'create-profile.html', context)


def profile_details(request):
    all_games = Game.objects.all()
    average = sum([game.rating for game in all_games]) / all_games.count()
    context = {
        'all_games': all_games,
        'average': average
    }
    return render(request, 'details-profile.html', context)


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
    all_games = Game.objects.all()
    if request.method == 'POST':
        profile.delete()
        all_games.delete()
        return redirect('home')
    return render(request, 'delete-profile.html')


def game_create(request):
    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'create-game.html', context)


def game_details(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        'game': game
    }
    return render(request, 'details-game.html', context)


def game_edit(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'GET':
        form = GameCreateForm(instance=game, initial=game.__dict__)
    else:
        form = GameCreateForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'game': game
    }
    return render(request, 'edit-game.html', context)


def game_delete(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'GET':
        form = GameDeleteForm(instance=game, initial=game.__dict__)
    else:
        game.delete()
        return redirect('dashboard')
    context = {
        'form': form,
        'game': game
    }
    return render(request, 'delete-game.html', context)

