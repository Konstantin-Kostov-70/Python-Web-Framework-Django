from Car.car_app.views import get_profile


def show_profile(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return context
