from django.urls import path 
from . import views
app_name = 'blacklists'

urlpatterns = [
    path('',views.index, name='index'),
]