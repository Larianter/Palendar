from django.shortcuts import render, redirect
from .models import Users, EventDetails, GroupCalendar
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.contrib import messages

current_user_id = None

# Create your views here.
def login(request):
    #render login page for palendar
    return render(request, 'palendar_app/logIn.html')

def register(request):
    #registers new user account
    if request.method == "POST":
        username = request.POST["new-username"]
        password = request.POST["new-password"]

        if Users.objects.filter(account_name=request.POST['new-username']).exists():
            messages.info(request, "Account name already in use.")
            return render(request, 'palendar_app/logIn.html', {'error_message': "Account name already in use."})
        else:
            new_user = Users(account_name = username, password = password)
            new_user.save()
            messages.info(request, "Account suecessfully created!")
            return render(request, 'palendar_app/logIn.html', {'error_message': "Account successfully created!"})
    
def inlogger(request):
    #logs the user in
    if request.method == "POST":
        if Users.objects.filter(account_name=request.POST['uname'], password=request.POST['psw']).exists():
            current_user = request.POST['uname']
            global current_user_id 
            current_user_id = Users.objects.get(account_name = current_user)
            response = redirect('personal-calendar')
        else:
            response = HttpResponse("credentials not found")
    else:
        response = redirect('login')

    return response

def personalCalendar(request):
    if current_user_id:
        user_events = EventDetails.objects.filter(userID=current_user_id)
        return render(request, 'palendar_app/personal_calendar.html', {'account_name': current_user_id.account_name,'user_events': user_events})
    else:
        return redirect('login')

def eventAdder(request):
    #adds event to calendar
    if request.method == "POST":
        eventName = request.POST["event-name"]
        eventDateTime = request.POST["event-dateTime"]
        eventDesc = request.POST["event-desc"]
        new_event = EventDetails(event_name = eventName, event_desc = eventDesc, event_date = eventDateTime, userID=current_user_id)
        new_event.save()

        return redirect('personal-calendar')
    
def settings(request):
    global current_user_id

    if current_user_id is None:
        return redirect('login')  # Redirect to login if user is not logged in

    try:
        # Fetch the User instance
        user = Users.objects.get(userID=current_user_id.userID)

        # Pass the username to the template
        return render(request, 'palendar_app/settings.html', {'account_name': user.account_name})
    except Users.DoesNotExist:
        return redirect('login')
    
def logOut(request): # We be logging out here
    global current_user_id 
    current_user_id = None
    return redirect('login')

def addEmail(request):                                              #Still need to add password changing
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user = Users.objects.get(userID=current_user_id.userID)

        #update user info
        if email:
            user.email = email
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name

        user.save()

        return render(request, 'palendar_app/settings.html', {
            'account_name': user.account_name,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'update_success': True
        })
    else:
        user = Users.objects.get(userID=current_user_id.userID)
        return render(request, 'palendar_app/settings.html', {
            'account_name': user.account_name,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        })

def delete_account(request):
    global current_user_id

    if request.method == "POST":
        try:
            # Find and delete the current user
            user = Users.objects.get(userID=current_user_id.userID)
            user.delete()
            
            # Clear the global current_user_id and redirect to login
            current_user_id = None
            return redirect('login')  # Redirect to login page after deletion
        except Users.DoesNotExist:
            return redirect('settings')  # Redirect to settings if user not found
    else:
        return HttpResponseBadRequest("Invalid request method.")

def groupCalendar(request):
    if current_user_id:
        group_members = GroupCalendar.objects.values_list('members', flat=True)
        group_events = EventDetails.objects.filter(userID__in=group_members)
        current_group = GroupCalendar.objects.get(members=current_user_id)
        return render(request, 'palendar_app/group_calendar.html', {'account_name': current_user_id.account_name,'group_events': group_events, 'group_calendar_name': current_group.group_name})
    else:
        return redirect('personal-calendar')
    
def createGroup(request):
    groupName = request.POST["group-name"]

    new_group = GroupCalendar(group_name = groupName)
    new_group.save()

    return redirect('personal-calendar')

def joinGroup(request):
    group_Name = request.POST["group-calendar-code"]
    try:
        group = GroupCalendar.objects.get(group_name = group_Name)
    except:
        return HttpResponse("Group Not Found")          #Placeholder... or is it?

    group.members.add(current_user_id)
    group.save()

    return redirect('personal-calendar')