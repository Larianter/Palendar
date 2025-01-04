from django.shortcuts import render

# Create your views here.
def login(request):
    #home and login page for palendar
    return render(request, 'palendar_app/logIn.html')