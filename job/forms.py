from django import forms
from django.forms import ModelForm
from job.admin import UserCreationForm
from Employer.models import MyUser
from django.contrib.auth.forms import PasswordResetForm


class RegisterForm(UserCreationForm):
    password1= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','style': "border:2px solid rgb(17, 72, 175) ; border-radius:5px;font-size:20px;",
                                            'placeholder': 'password'}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': "border:2px solid rgb(17, 72, 175);border-radius:5px;font-size:20px",
               'placeholder': 'confirm password'}))
    class Meta:
        model=MyUser
        fields=['email','password1','password2','role']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control','style':"border:2px solid rgb(17, 72, 175);border-radius:5px;font-size:20px",'placeholder':'e-mail'}),
            'role':forms.Select(attrs={'class': 'form-control','style':"border:2px solid rgb(17, 72, 175);border-radius:4px;font-size:20px",'placeholder':'password'})
        }
class LoginForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','style': "border:2px solid rgb(17, 72, 175) ; border-radius:5px;font-size:20px;width:100%",
                                            'placeholder': 'email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','style': "border:2px solid rgb(17, 72, 175) ; border-radius:5px;font-size:20px;width:100%",
                                            'placeholder': 'password','autocomplete':"current-password"}))


class ResetpasswordForm(PasswordResetForm):
    def __init__(self,*args,**kwargs):
        super(ResetpasswordForm,self).__init__(*args,**kwargs)
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))