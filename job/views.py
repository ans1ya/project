from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,UpdateView,ListView
from job.forms import LoginForm,RegisterForm
from Employer.models import MyUser,Jobs,CompanyProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView


# Create your views here.
def index(request):
    return render(request,'index.html')

class SignupView(View):
    def get(self,request,*args,**kwargs):
        form=RegisterForm()
        context={'form':form}
        return render(request,'signup.html',context)
    def post(self,request,*args,**kwargs):
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context={'form':form}
            return render(request,'signup.html',context)

class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        context={'form':form}
        return render(request,'login.html',context)
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            role=form.cleaned_data.get('role')
            user=authenticate(request,email=email,password=password,role=role)
            if user:
                login(request,user)
                if user.role == 'employer':
                    return redirect('ehome')
                else:
                    return redirect('c_home')
            else:
                messages.warning(request,'Please enter a valid username or password')
                return render(request,'login.html')
        else:
            context={'form':form}
            return render(request,'login.html',context)

def SignoutView(request):
    logout(request)
    return redirect('index')

# class ChangePasswordView(PasswordChangeView):
#     form_class = PasswordChangeForm
#     template_name = 'changepassword.html'
#     success_url = reverse_lazy('password_success')
#
# def PasswordSuccess(request):
#     messages.success(request, 'Password has been changed successfully,Please login with new password')
#     return render(request,'password_success.html',messages)
class SearchView(ListView):
    model=Jobs
    template_name = 'search.html'
    def get(self, request, *args, **kwargs):
        query =request.GET.get("search")
        if query:
            jobs=Jobs.objects.filter(Q(location__icontains=query)|Q(job_title__icontains=query))
            context={'jobs':jobs}
            return render(request,'search.html',context)
        else:
            jobs=Jobs.objects.all()
            context={'jobs':jobs}
            return render(request,'index.html',context)

    # def post(self, request):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # user = form.save(commit=False)  # it doesnot save in database, it is used to et clean the values
    #         # clean data
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #
    #         # authenticate user:
    #         user = authenticate(username=username, password=password)
    #
    #         if user is not None:
    #             login(request, user)
    #             if (request.user.is_prof == True):
    #                 return redirect('essay:file', )
    #             else:
    #                 return redirect('essay:stdprofile')
    #         else:
    #             return render(request, self.template_name, {
    #                 'error_message': ' Login Failed! Enter the username and password correctly', })
    #     else:
    #         msg = 'Errors: %s' % form.errors.as_text()
    #         return HttpResponse(msg, status=400)
    #
    #     return render(request, self.template_name, {'form': form})
