from datetime import datetime

from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home page',
        'date': datetime.now(),
        'students': [
            'Sofia',
            'Maria',
            'Petar',
        ],
        'values': list(range(20))
    }
    return render(request, 'index.html', context)


def get_students(request):
    context = {
        'students': [
            'Sofia',
            'Maria',
            'Petar',
        ],
    }
    return render(request, 'students.html', context)


def get_values(request):
    context ={
        'values': list(range(20))
    }
    return render(request, 'values.html', context)


def get_articles(request):
    return render(request, 'show_articles.html')
