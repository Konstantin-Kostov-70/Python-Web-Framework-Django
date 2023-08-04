from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from AuthenticationWebApp.auth_web_app.forms import SignUpForm


def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'index.html', context)


class SignUpView(CreateView):
    template_name = 'auth-form.html'
    form_class = SignUpForm

    success_url = reverse_lazy('index')


def sign_up(request):
    if request.method == 'GET':
        form = SignUpForm()
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
        }
    return render(request, 'auth-form-fbv.html', context)


class SignInView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('index')


class SignOutView(LogoutView):
    next_page = reverse_lazy('index')


