#Define URL patterns for palendar

from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name='login'), #login page
    path("register", views.register, name='register'), #registration
    path("login", views.inlogger, name='inlogger'), #logging in
    path("add_event", views.eventAdder, name='eventAdder'), #event creation
    path("personal-calendar", views.personalCalendar, name='personal-calendar'),
    path("settings", views.settings, name='settings'), #account settings
    path("update_settings", views.addEmail, name='addEmail'),
    path("delete_account", views.delete_account, name='delete_account'),
    path("logout", views.logOut, name='logout'),
    path("group-calendar", views.groupCalendar, name='group-calendar')
]
