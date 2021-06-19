from django.shortcuts import render, redirect
from .models import ClientAssessment
from .forms import OnsiteForm

# Create your views here.

def ReadView(request):
    #check to see if user is authenticated
    if request.user.is_authenticated is True:
        user = request.user
    else:
        #return back to the login page
        return redirect('/register/login/')
    onsitelist = ClientAssessment.objects.filter(user=user)
    context = {
        'onsitelist' : onsitelist 
    }
    return render(request, 'templates/overview.html', context)

def CreateView(request):
    #Check to see if user is logged in 
    if request.user.is_authenticated is True:
        user = request.user
    else:
        #redirect back to the login page
        return redirect('/register/login/')
    #create a form to enter data and POST to the database
    if request.method == 'POST':
        form = OnsiteForm(request.POST)
        #check to see if form is valid
        if form.is_valid():
            #process the data from models.py in form.cleaned_data format 
            itemlist=ClientAssessment(
                user=user,
                client_name=form.cleaned_data['client_name'],
                assessment_location=form.cleaned_data['assessment_location'],
                assessment_date=form.cleaned_data['assessment_date'],
                change_in_status=form.cleaned_data['change_in_status'],
                status_overview=form.cleaned_data['status_overview'],
                services_implemented=form.cleaned_data['services_implemented'],
                services_overivew=form.cleaned_data['services_overivew'],
                change_in_plan=form.cleaned_data['change_in_plan'],
                plan_overview=form.cleaned_data['plan_overview'],
            )
            #save the data
            itemlist.save()
            #redirect back to homepage
            return redirect('/')
    else:
        
        #else get an empty form
        form = OnsiteForm()
    context = {'form': form}
    return render(request, 'onsitetool/create.html', context)


            


    



