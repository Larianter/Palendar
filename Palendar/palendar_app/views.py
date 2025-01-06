from django.shortcuts import render, redirect
from .models import Users
from django.http import HttpResponse

# Create your views here.
def login(request):
    #render login page for palendar
    return render(request, 'palendar_app/logIn.html')

def register(request):
    if request.method == "POST":
        username = request.POST["new-username"]
        password = request.POST["new-password"]

        new_user = Users(account_name = username, password = password)
        new_user.save()
        
        return redirect('login')
    
def inlogger(request):
    if request.method == "POST":
        if Users.objects.filter(account_name=request.POST['uname'], password=request.POST['psw']).exists() == True:
            response = HttpResponse("credentials accepted")
        else:
            response = HttpResponse("credentials not found")

    return response
