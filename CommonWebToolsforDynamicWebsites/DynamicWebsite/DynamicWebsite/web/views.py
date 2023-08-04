import random
from time import sleep

from django.db import OperationalError
from django.shortcuts import render
from django.views.decorators.cache import cache_page

"""
    This function make simulation for very slow operation 
    who need 15 seconds for loading the page.
"""


def very_slow_operation():
    sleep(1.5)
    return random.randint(10, 99)


LATEST_VALUES_SESSION_KEY = 'LATEST_VALUES_SESSION_KEY'


def show_session_id(request):
    num1 = 0
    num2 = 0
    num3 = 0
    latest_value = []
    value = random.randint(10, 99)
    try:
        latest_value = request.session.get(LATEST_VALUES_SESSION_KEY, [])
        latest_value = [value] + latest_value
        latest_value = latest_value[:3]
        request.session[LATEST_VALUES_SESSION_KEY] = latest_value
    except OperationalError:
        latest_value = [value] + latest_value

    num1 = latest_value[0]

    if len(latest_value) >= 2:
        num2 = latest_value[1]
    if len(latest_value) >= 3:
        num3 = latest_value[2]

    contex = {
        'value': value,
        'num1': num1,
        'num2': num2,
        'num3': num3
    }
    return render(request, 'session.html', contex)


@cache_page(1 * 10)
def index(request):
    value = very_slow_operation()
    context = {
        'value': value
    }
    return render(request, 'index.html', context)
