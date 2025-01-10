from django.contrib import admin
from palendar_app.models import EventDetails, Users, GroupCalendar
# Register your models here.
admin.site.register(EventDetails)
admin.site.register(Users)
admin.site.register(GroupCalendar)