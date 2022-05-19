from django.shortcuts import render,redirect
from Employer.models import MyUser,Jobs,CompanyProfile
from Candidate.models import Applicant,Applications
from Candidate.forms import CandidateprofileForm,SearchForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,TemplateView
from Candidate.filters import JobFilter
from datetime import date
from django.utils.decorators import method_decorator
from job.decorators import sign_in_required
from django.core.paginator import Paginator
from Employer.forms import ProcessForm
# Create your views here.
@method_decorator(sign_in_required,name='dispatch')
class CandidateHome(View):
    def get(self,request,*args,**kwargs):
        return render(request,'c_home.html')
@method_decorator(sign_in_required,name='dispatch')
class JoblistView(ListView):
    model = Jobs
    template_name = 'joblist.html'
    context_object_name = 'jobs'
    def get(self, request, *args, **kwargs):
        qs=Jobs.objects.all().order_by("-create_date")
        f=JobFilter(request.GET,queryset=Jobs.objects.all().order_by("-create_date"))
        paginator = Paginator(qs,4)
        page_number = request.GET.get('page')
        qs= paginator.get_page(page_number)
        context={'jobs':qs,'filter':f}
        return render(request,'joblist.html',context)


@method_decorator(sign_in_required,name='dispatch')
class JobdetailView(DetailView):
    model = Jobs
    template_name = 'job_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'job'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        applicant=Applicant.objects.get(applicant__email=self.request.user)
        qs=Applications.objects.filter(applicant=applicant,job=self.kwargs['id']).count()
        if qs>0:
            context['applied']=True
        else:
            context['applied']=False

        return context



@method_decorator(sign_in_required,name='dispatch')
class AddprofileView(CreateView):
    model = Applicant
    template_name = 'c_profile.html'
    form_class = CandidateprofileForm
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            # print('here')
            profile=form.save(commit=False)
            # print(request.user.id)
            profile.applicant=request.user
            profile.save()
            return redirect('c_home')
        else:
            context={'form':form}
            return render(request,self.template_name,context)

@method_decorator(sign_in_required,name='dispatch')
class ProfileView(DetailView):
    model = Applicant
    template_name = 'c_viewprofile.html'
    def get(self,request,*args,**kwargs):
        profile=Applicant.objects.get(applicant=request.user)
        context={'profile':profile}
        return render(request,self.template_name,context)

@method_decorator(sign_in_required,name='dispatch')
class EditprofileView(UpdateView):
    model = Applicant
    form_class = CandidateprofileForm
    template_name = 'profileedit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('c_viewprofile')

@method_decorator(sign_in_required,name='dispatch')
class JobapplyView(View):
    def get(self, request, *args, **kwargs):
        id=kwargs['id']
        job=Jobs.objects.get(id=id)
        applicant=Applicant.objects.get(applicant=request.user)
        # Applicant.applicant=request.user
        # applicant=Applications.applicant
        application=Applications(applicant=applicant,job=job)
        application.save()
        messages.success(request,'You have successfully applied')
        return redirect('c_joblist')

@method_decorator(sign_in_required,name='dispatch')
class AppliedJobsView(ListView):
    model = Applications
    template_name = 'appliedjobs.html'
    context_object_name = 'applications'
    def get(self,request,*args,**kwargs):
        applicant=Applicant.objects.get(applicant=request.user)
        applied_job=Applications.objects.filter(applicant=applicant).order_by('-submitted_date')
        context={'applications':applied_job}
        return render(request,self.template_name,context)
class Searchindex(TemplateView):
    template_name = 'search_index.html'


@method_decorator(sign_in_required,name='dispatch')
def JobSearchView(request):
    qs=Jobs.objects.all()
    job_title=request.GET.get('job_title')
    skills=request.GET.get('skills')
    location=request.GET.get('location')

    qs=qs.filter(job_title__icontains=job_title)
    qs=qs.filter(skills__icontains=skills)
    qs=qs.filter(location__icontains=location)
    context={'queryset':qs}
    return render(request,'joblist.html',context)

@method_decorator(sign_in_required,name='dispatch')
class NotificationView(CreateView):
    model = Applications
    form_class = ProcessForm
    template_name = 'notification.html'
    pk_url_kwarg = 'id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        applicant=Applicant.objects.get(applicant=self.request.user)
        qs = Applications.objects.all().filter(applicant=applicant)
        accepted = qs.filter(status='accepted')
        rejected = qs.filter(status='rejected')
        under_processing = qs.filter(status='under_processing')

        context['accepted'] = accepted
        context['rejected'] = rejected
        context['under_processing'] = under_processing
        context['application'] = self.object
        return context


