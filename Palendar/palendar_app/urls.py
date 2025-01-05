#Define URL patterns for palendar

from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name='login'), #login page
    path("register", views.register, name='register'),
]
