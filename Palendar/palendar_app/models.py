from django.db import models

# Create your models here.
class Users(models.Model):
    #stores user account data
    userID = models.IntegerField(primary_key=True)
    account_name = models.CharField(max_length=24)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=12)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

class User_Calendar(models.Model):
    #stores users own events
    eventID = models.IntegerField(primary_key=True)
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)

class Event_Details(models.Model):
    #data about user events
    event_name = models.CharField(max_length=16)
    event_desc = models.CharField(max_length=128)
    event_date = models.DateTimeField(null=False)
    eventID = models.ForeignKey(User_Calendar, on_delete=models.CASCADE)
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)

class Group_Calendar(models.Model):
    #stores all users' events in group
    groupID = models.IntegerField(primary_key=True)
    members = models.ForeignKey(Users, on_delete=models.CASCADE)
    eventID = models.ForeignKey(User_Calendar, on_delete=models.CASCADE)