from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('templates/', include('DjangoTemplates.templates_app.urls'))
]
