from django.urls import path
from DynamicWebsite.web.views import index, show_session_id

urlpatterns = [
   path('', index, name='index'),
   path('session/', show_session_id, name='session')
]