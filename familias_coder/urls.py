from django.urls import include, path
from .views import person_list

urlpatterns = [
     path('alumnos/', person_list)
]