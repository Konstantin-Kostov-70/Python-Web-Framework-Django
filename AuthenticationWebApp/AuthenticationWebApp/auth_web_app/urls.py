from django.urls import path
from AuthenticationWebApp.auth_web_app.views import index, SignUpView, sign_up, SignInView, SignOutView

urlpatterns = [
    path('', index, name='index'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-up/form/', sign_up, name='sign-up-form'),
    path('sign-in/form/', SignInView.as_view(), name='sign-in-form'),
    path('sign-out', SignOutView.as_view(), name='sign-out'),


]
