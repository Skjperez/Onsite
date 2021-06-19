from django import forms

class OnsiteForm(forms.Form):
    client_name = forms.CharField(label='Client Name',max_length=50)
    assessment_location = forms.CharField(label='Assessment Location',max_length=50)
    assessment_date = forms.DateField()
    change_in_status = forms.BooleanField()
    status_overview = forms.CharField(widget=forms.Textarea)
    services_implemented = forms.BooleanField()
    services_overivew = forms.CharField(widget=forms.Textarea)
    change_in_plan = forms.BooleanField()
    plan_overview= forms.CharField(widget=forms.Textarea)