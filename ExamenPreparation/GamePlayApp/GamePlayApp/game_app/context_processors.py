from GamePlayApp.game_app.models import Profile


def show_profile(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile,
        'Hello': 'Hello'
    }
    return context
