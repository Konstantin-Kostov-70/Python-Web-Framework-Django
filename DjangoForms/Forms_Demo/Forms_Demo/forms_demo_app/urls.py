from django.urls import path

from Forms_Demo.forms_demo_app.views import index, model_forms_view, relationship_demo

urlpatterns = [
   path('', index, name='home'),
   path('model-forms/', model_forms_view, name='model-forms'),
   path('relation-demo/', relationship_demo, name='relation'),
]