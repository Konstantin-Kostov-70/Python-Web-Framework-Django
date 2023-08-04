from FruitipediaApp.fruit_app.models import ProfileModel


def show_profile(request):
    profile = ProfileModel.objects.first()
    context = {
        'profile': profile
    }
    return context
