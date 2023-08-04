from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('department/', include('Urls_and_Views.department.urls'))
]
