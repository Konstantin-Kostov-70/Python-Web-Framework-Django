import random
from time import sleep

from django.db import OperationalError
from django.shortcuts import render
from django.views.decorators.cache import cache_page

"""
    This function make simulation for very slow operation 
    who need 1.5 seconds for loading the page.
"""


def very_slow_operation():
    sleep(1.5)
    return random.randint(10, 99)


"""
    This function represent how session work and we can save the information
    in session and use after then.In this case we save the last three value
    from the random function
"""

LATEST_VALUES_SESSION_KEY = 'LATEST_VALUES_SESSION_KEY'


def show_session_id(request):
    num2 = 0
    num3 = 0

    value = random.randint(10, 99)
    latest_value = request.session.get(LATEST_VALUES_SESSION_KEY, [])
    latest_value = [value] + latest_value
    latest_value = latest_value[:3]
    request.session[LATEST_VALUES_SESSION_KEY] = latest_value

    if len(latest_value) >= 2:
        num2 = latest_value[1]
    if len(latest_value) >= 3:
        num3 = latest_value[2]

    contex = {
        'value': value,
        'num1': latest_value[0],
        'num2': num2,
        'num3': num3
    }
    return render(request, 'session.html', contex)


"""
In this function we represent how work cache.In this case we can
reload page after 10 seconds because page is cached
"""


@cache_page(1 * 10)
def index(request):
    value = very_slow_operation()
    context = {
        'value': value
    }
    return render(request, 'index.html', context)
