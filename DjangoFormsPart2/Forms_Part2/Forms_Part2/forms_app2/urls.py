from django.urls import path

from Forms_Part2.forms_app2.views import validate_form_view, model_form_validate_view, create_person_view, list_person

urlpatterns = [
   path('', validate_form_view, name='home'),
   path('model-form', model_form_validate_view, name='model form'),
   path('person/', create_person_view, name='person'),
   path('list_person', list_person, name='list person')
]