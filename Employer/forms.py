from django import forms
from django.forms import ModelForm
from Employer.models import MyUser,CompanyProfile,Jobs
from Candidate.models import Applications
from django.contrib.auth.forms import PasswordChangeForm

class ProfileForm(ModelForm):
        class Meta:
            model = CompanyProfile
            exclude=('company',)
            widgets = {

                # 'company': forms.TextInput(attrs={'class': 'form-control'}),
                # 'company_logo': forms.FileInput(attrs={'class': 'form-control'}),
                'recruter_name': forms.TextInput(attrs={'class': 'form-control'}),
                'Designation': forms.Select(attrs={'class': 'form-select'}),
                'services': forms.Select(attrs={'class': 'form-select'}),
                'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                'number_of_employees': forms.Select(attrs={'class': 'form-select'}),
                'website': forms.TextInput(attrs={'class': 'form-control'}),
                'Bio': forms.Textarea(attrs={'class': 'form-control'})
            }

class AddjobForm(ModelForm):
    class Meta:
        model=Jobs
        exclude = ('company',)
        widgets = {
            'job_title':forms.TextInput(attrs={'class':'form-control'}),
            'salary':forms.TextInput(attrs={'class':'form-control'}),
            # 'image':forms.FileInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'experience':forms.NumberInput(attrs={'class':'form-control','placeholder':'experience in years'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'skills':forms.Textarea(attrs={'class':'form-control'}),
            'vacancies':forms.NumberInput(attrs={'class':'form-control'}),
            'create_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'end_date':forms.DateInput(attrs={'class':'form-control','type':'date'})

        }

class ProcessForm(ModelForm):
    options = (
        ('accepted', 'accepted'),
        ('rejected', 'rejected'),
        ('under_processing', 'under_processing'),
    )
    status = forms.ChoiceField(choices=options)

    class Meta:
        model = Applications
        fields = ['status','status_updated_date']
        widgets = {

            'status': forms.Select(attrs={'class': 'form-control'}),
            'status_updated_date':forms.DateInput(attrs={'class':'form-control','type':'date'})

        }

class MyPasswordchangeForm(PasswordChangeForm):
    def __init__(self,*args,**kwargs):
        super(MyPasswordchangeForm,self).__init__(*args,**kwargs)
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


