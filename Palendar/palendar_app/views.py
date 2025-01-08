from django.shortcuts import render, redirect
from .models import Users, Event_Details, User_Calendar
from django.http import HttpResponse

# Create your views here.
def login(request):
    #render login page for palendar
    return render(request, 'palendar_app/logIn.html')

def register(request):
    #registers new user account
    if request.method == "POST":
        username = request.POST["new-username"]
        password = request.POST["new-password"]

        new_user = Users(account_name = username, password = password)
        new_user.save()
        
        return redirect('login')
    
def inlogger(request):
    #logs the user in
    if request.method == "POST":
        if Users.objects.filter(account_name=request.POST['uname'], password=request.POST['psw']).exists() == True:
            current_user = request.POST['uname']
            current_user_id = Users.objects.get(account_name = current_user)
            user_events = Event_Details.objects.filter(eventID__in=User_Calendar.objects.filter(userID=current_user_id))
            current_events = "\n".join([str(event) for event in user_events])
            response = render(request, 'palendar_app/personal_calendar.html', {'account_name': current_user,'DEBUG_TEST': current_events})
        else:
            response = HttpResponse("credentials not found")

    return response

def eventAdder(request):
    #adds event to calendar
    if request.method == "POST":
        eventName = request.POST["event-name"]
        eventDateTime = request.POST["event-dateTime"]
        eventDesc = request.POST["event-desc"]
        newEventID = User_Calendar.objects.order_by("eventID")[0] + 1

        new_event = Event_Details(event_name = eventName, event_dateTime = eventDateTime, event_desc = eventDesc, eventID = newEventID)
        new_event.save()

        return redirect('palendar_app/personal_calendar.html')

