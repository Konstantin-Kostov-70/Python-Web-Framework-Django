from Frutipedia.fruit_app.views import get_profile


def profile_context(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return context
