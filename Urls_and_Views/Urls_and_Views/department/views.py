from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def sample_view(request, *args, **kwargs):
    print(f'args: {args}')
    print(f'kwarg: {kwargs}')
    return HttpResponse(f'Hello sample view {kwargs.get("department_id")}')
