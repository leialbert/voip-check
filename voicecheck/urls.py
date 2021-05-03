from django.urls import path 
from . import views
app_name = 'voicecheck'

urlpatterns = [
    path('',views.index, name='index'),
]