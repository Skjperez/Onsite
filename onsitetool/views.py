from django.shortcuts import render, redirect
from .models import ClientAssessment
from .forms import OnsiteForm
from django.shortcuts import Http404

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
    return render(request, 'onsitetool/read.html', context)

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
                services_overview=form.cleaned_data['services_overview'],
                change_in_plan=form.cleaned_data['change_in_plan'],
                plan_overview=form.cleaned_data['plan_overview'],
            )
            #save the data
            itemlist.save()
            #redirect back to homepage
            return redirect('/onsitetool/read/')
    else:
        
        #else get an empty form
        form = OnsiteForm()
    context = {'form': form}
    return render(request, 'onsitetool/create.html', context)

def ReviewView(request, client_id):
    try:
        #get the specific client's onsite tool by id
        individual = ClientAssessment.objects.get(id=client_id)
    #get error if the client does not exist
    except ClientAssessment.DoesNotExist:
        raise Http404('Client Onsite Tool Does Not Exist')
    context = {
        'individual' : individual 
    }
    return render(request, 'onsitetool/review.html', context)

def DeleteView(request, client_id):
    #get specific client's onsite tool by id
    individual = ClientAssessment.objects.get(id=client_id)
    #delete client onsite tool entry
    individual.delete()
    #redirect back to the main page
    return redirect('/onsitetool/read/')

def UpdateView(request, client_id):
    #get specific client onsite tool by id
    individual = ClientAssessment.objects.get(id=client_id)
    #generate form with data pre-populated
    form = OnsiteForm(
        initial = {
           'client_name' : individual.client_name,
            'assessment_location' : individual.assessment_location,
            'assessment_date' : individual.assessment_date,
            'change_in_status' : individual.change_in_status,
            'status_overview' : individual.status_overview,
            'services_implemented' : individual.services_implemented,
            'services_overview' : individual.services_overview,
            'change_in_plan' : individual.change_in_plan,
            'plan_overview' : individual.plan_overview,

        }
    )
    context = {
        'individual' : individual,
        'form' : form,

    }
    #save form with updated data 
    if request.method == 'POST':
        form = OnsiteForm(request.POST)
        if form.is_valid():
            individual.client_name = form.cleaned_data["client_name"]
            individual.assessment_location = form.cleaned_data["assessment_location"]
            individual.assessment_date = form.cleaned_data["assessment_date"]
            individual.change_in_status = form.cleaned_data["change_in_status"]
            individual.status_overview = form.cleaned_data["status_overview"]
            individual.services_implemented = form.cleaned_data["services_implemented"]
            individual.services_overview = form.cleaned_data["services_overview"]
            individual.change_in_plan = form.cleaned_data["change_in_plan"]
            individual.plan_overview = form.cleaned_data["plan_overview"]
            individual.save()
            #redirect back to the review page
            return redirect(f'/onsitetool/{client_id}')
    return render(request, 'onsitetool/update.html', context)
            
            





            


    



