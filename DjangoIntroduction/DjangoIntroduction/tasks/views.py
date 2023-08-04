from django.http import HttpResponse
from django.shortcuts import render

from DjangoIntroduction.tasks.models import Task


def index(request):
    return render(request, 'index.html')


def get_all_tasks(request):
    all_tasks = Task.objects.all()
    context = {
        'title': 'All tasks',
        'all_tasks': all_tasks
    }
    return render(request, 'all-tasks.html', context)
