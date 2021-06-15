from django.shortcuts import render
from django.contrib.auth import login, authenticate 
from django.contrib.auth import logout

# Create your views here.
def UserLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        #Redirect to home page
    else:
        #Return message 'invalid login'

def UserLogout(request):
    logout(request)
    #Redirect to login page
