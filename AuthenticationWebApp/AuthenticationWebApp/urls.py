from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AuthenticationWebApp.auth_web_app.urls'))
]
