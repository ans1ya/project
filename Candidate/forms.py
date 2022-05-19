from django import forms
from django.forms import ModelForm
from Candidate.models import Applicant,Applications
from Employer.models import Jobs

class CandidateprofileForm(ModelForm):
    class Meta:
        model=Applicant
        exclude= ('applicant',)
        widgets={
            'applicant_name':forms.TextInput(attrs={'class':'form-control'}),
            # 'profile_pic':forms.FileInput(attrs={'class':'form-control'}),
            'qualification':forms.TextInput(attrs={'class':'form-control'}),
            'experience':forms.Select(attrs={'class':'form-control'}),
            'skills':forms.Textarea(attrs={'class':'form-control'}),
            # 'resume':forms.FileInput(attrs={'class':'form-control'})
        }
class SearchForm(forms.ModelForm):
    class Meta:
        model=Jobs
        fields=['job_title','skills','location']
        widgets={
            'job_title':forms.Select(attrs={'class':'form-control'}),
            'skills':forms.Select(attrs={'class':'form-control'}),
            'location':forms.Select(attrs={'class':'form-control'})
        }


