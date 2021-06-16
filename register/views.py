from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate 
from django.contrib.auth import logout
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def UserLogin(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data('username')
            username.save()
            return redirect('/')
    else:
        pass
    form = NewUserForm()
    context = {'form' : form}
    return render(request, 'registration/login.html', context)

        #form = AuthenticationForm(request, data=request.POST)
        #if form.is_valid():
            #username = form.cleaned_data.get('username')
            #password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=password)
            #if user is not None:
                #login(request, user)
                ##Redirect to home page
                #return redirect('/')
            #else:
                #messages.error(request,'Invalid username or password')
            #return render(request)
            
    
	
        

def UserLogout(request):
    logout(request)
    #Redirect to login page
    return redirect('/register/login/')

def Signup(request):
    return render(request, 'registration/signup.html', {'form' : UserCreationForm()})
    
