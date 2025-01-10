from django.db import models

# Create your models here.
class Users(models.Model):
    #stores user account data
    userID = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=12)
    email = models.CharField(max_length=64, null=True, blank=True)
    password = models.CharField(max_length=16)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)

class EventDetails(models.Model):
    #data about user events
    eventID = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=24)
    event_desc = models.CharField(max_length=128)
    event_date = models.DateTimeField(null=False)
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.event_name} | Description: {self.event_desc} |\n Date: {self.event_date}"

class GroupCalendar(models.Model):
    #stores all users' events in group
    groupID = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=24)
    members = models.ForeignKey(Users, on_delete=models.CASCADE)
    eventID = models.ForeignKey(EventDetails, on_delete=models.CASCADE)