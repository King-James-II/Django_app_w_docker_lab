from django.urls import path
from . import views

# Define URL patterns

urlpatterns = [
    # URL pattern for the index view
    path(route='', view=views.index, name='index'),
    # URL pattern for the get_date view
    path(route='date', view=views.get_date, name='date'),
]