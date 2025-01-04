from django.contrib import admin
from palendar_app.models import User_Calendar, Event_Details, Users, Group_Calendar
# Register your models here.
admin.site.register(User_Calendar)
admin.site.register(Event_Details)
admin.site.register(Users)
admin.site.register(Group_Calendar)