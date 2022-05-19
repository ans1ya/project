from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,UpdateView,ListView,DetailView
from Employer.forms import ProfileForm,AddjobForm,ProcessForm,MyPasswordchangeForm
from Employer.models import MyUser,Jobs,CompanyProfile
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib import messages
from Candidate.models import Applications,Applicant
from django.db.models import Q
from datetime import date
from django.utils.decorators import method_decorator
from job.decorators import sign_in_required
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.core.paginator import Paginator
from django.core.mail import send_mail
# Create your views here.



@method_decorator(sign_in_required,name='dispatch')
def HomeView(request):
    return render(request,'ehome.html')

@method_decorator(sign_in_required,name='dispatch')
class AddProfileView(CreateView):
    model = CompanyProfile
    form_class =ProfileForm
    template_name = 'addprofile.html'
    context_object_name = 'profile'
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            company=request.user
            profile.company=company
            profile.user=request.user
            profile.save()
            return redirect('ehome')
        else:
            context={'form':form}
            return render(request,self.template_name,context)

@method_decorator(sign_in_required,name='dispatch')
class ViewProfile(DetailView):
    model=CompanyProfile
    template_name = 'viewprofile.html'
    def get(self,request,*args,**kwargs):
        qs=self.model.objects.get(company=self.request.user)
        context={'profile':qs}
        return render(request,self.template_name,context)

@method_decorator(sign_in_required,name='dispatch')
class EditprofileView(UpdateView):
    model = CompanyProfile
    template_name = 'editprofile.html'
    form_class = ProfileForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('viewprofile')

@method_decorator(sign_in_required,name='dispatch')
class AddjobView(CreateView):
    model = Jobs
    form_class = AddjobForm
    template_name = 'addjob.html'
    context_object_name = 'job'
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            job=form.save(commit=False)
            company=CompanyProfile.objects.get(company=request.user)
            job.company=company
            job.save()
            return redirect('listjob')
        else:
            return render(request,self.template_name,{'form':form})

@method_decorator(sign_in_required,name='dispatch')
class ListJobView(ListView):
    model = Jobs
    context_object_name = 'jobs'
    template_name = 'listjob.html'
    def get(self,request,*args,**kwargs):
        company=request.user.employer
        today = date.today()
        jobs=Jobs.objects.filter(company=company,end_date__gt=today).order_by('-create_date')
        paginator = Paginator(jobs, 3)
        page_number = request.GET.get('page')
        jobs = paginator.get_page(page_number)
        return render(request,self.template_name,{'jobs':jobs})

@method_decorator(sign_in_required,name='dispatch')
class ExpiredJobs(ListView):
    model = Jobs
    context_object_name = 'jobs'
    template_name = 'expiredjobs.html'
    def get(self,request,*args,**kwargs):
        company = request.user.employer
        today = date.today()
        jobs = Jobs.objects.filter(company=company, end_date__lt=today).order_by('-create_date')
        return render(request, self.template_name, {'jobs': jobs})


@method_decorator(sign_in_required,name='dispatch')
class EditJobView(UpdateView):
    model = Jobs
    form_class = AddjobForm
    template_name ='editjob.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listjob')

@method_decorator(sign_in_required,name='dispatch')
class Jobdetail(DetailView):
    model = Jobs
    template_name = 'jobdetail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'job'

@method_decorator(sign_in_required,name='dispatch')
class ListApplications(ListView):
    model = Applications
    template_name = 'listapplication.html'
    context_object_name = 'applications'
    def get(self,request,*args,**kwargs):
        company=CompanyProfile.objects.get(company=request.user)
        job=Jobs.objects.filter(company=company)
        applications=Applications.objects.order_by('-submitted_date')
        # f=JobFilter(request.GET,queryset=job)
        paginator = Paginator(applications,6)
        page_number = request.GET.get('page')
        applications = paginator.get_page(page_number)
        context={'applications':applications}
        return render(request,self.template_name,context)

# def listing(request):
#     contact_list = Contact.objects.all()
#     paginator = Paginator(contact_list, 25) # Show 25 contacts per page.
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'list.html', {'page_obj': page_obj})
@method_decorator(sign_in_required,name='dispatch')
class ApplicantList(ListView):
    model = Applications
    context_object_name = 'applicants'
    template_name = 'applicant.html'
    def get(self, request, *args, **kwargs):
        id=kwargs['id']
        job=Jobs.objects.get(id=id)
        qs=Applications.objects.filter(job=job).order_by('-submitted_date')
        context={'applicants':qs}
        return render(request,'applicant.html',context)


@method_decorator(sign_in_required,name='dispatch')
class ApplicantDetail(DetailView):
    model = Applications
    template_name = 'applicant_detail.html'
    pk_url_kwarg = 'id'
    def get(self,request,*args,**kwargs):
        id=kwargs['id']
        applicant=Applicant.objects.get(id=id)
        context={'applicant':applicant}
        return render(request,self.template_name,context)

@method_decorator(sign_in_required,name='dispatch')
class ApplicationSummary(ListView):
    model = Applications
    context_object_name = 'applications'
    template_name = 'application_summary.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        qs = Applications.objects.all()
        accepted = qs.filter(status='accepted')
        rejected = qs.filter(status='rejected')
        under_processing = qs.filter(status='under_processing')

        context['accepted'] = accepted
        context['rejected'] = rejected
        context['under_processing'] = under_processing
        # context['n_count']=n_count
        return context

@method_decorator(sign_in_required,name='dispatch')
class ProcessApplication(UpdateView):
    model = Applications
    form_class = ProcessForm
    template_name = 'process_application.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listapplications')
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs=Applications.objects.all()
        accepted=qs.filter(status='accepted')
        rejected=qs.filter(status='rejected')
        under_processing=qs.filter(status='under_processing')

        context['accepted']=accepted
        context['rejected']=rejected
        context['under_processing']=under_processing
        context['application']=self.object
        return context









