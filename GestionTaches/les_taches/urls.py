from django.urls import path
from . import views

urlpatterns = [
    path('home/<name>', views.home, name='home'),
]