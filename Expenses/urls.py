# basic URL Configurations
from django.urls import  path
from . import views

# specify URL Path for rest_framework
urlpatterns = [
	path('create/', views.add_item, name='add-items'),
]
