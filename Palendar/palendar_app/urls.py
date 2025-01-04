#Define URL patterns for palendar

from django.urls import path
from . import views

urlpatterns = [
    #home page(login)
    path("", views.login, name='login'),
]