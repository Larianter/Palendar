#Define URL patterns for palendar

from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name='login'), #login page
    path("register", views.register, name='register'), #registration
    path("login", views.inlogger, name='inlogger'), #logging in
    path("add_event", views.eventAdder, name= 'eventAdder'), #event creation
]
