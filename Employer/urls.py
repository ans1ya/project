from django.urls import path,reverse_lazy
from Employer import views
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from Employer.forms import MyPasswordchangeForm


urlpatterns=[
    path('',views.HomeView,name='ehome'),
    path('addprofile/',views.AddProfileView.as_view(),name='addprofile'),
    path('viewprofile/',views.ViewProfile.as_view(),name='viewprofile'),
    path('editprofile/<int:id>',views.EditprofileView.as_view(),name='editprofile'),
    path('add_job/',views.AddjobView.as_view(),name='addjob'),
    path('list_job/',views.ListJobView.as_view(),name='listjob'),
    path('edit_job/<int:id>',views.EditJobView.as_view(),name='editjob'),
    path('jobdetail/<int:id>',views.Jobdetail.as_view(),name='jobdetail'),
    path('listapplications',views.ListApplications.as_view(),name='listapplications'),
    path('applicantdetail,<int:id>',views.ApplicantDetail.as_view(),name='applicant_detail'),
    path('applicantlist/<int:id>',views.ApplicantList.as_view(),name="applicantlist"),
    path('expiredjobs',views.ExpiredJobs.as_view(),name='expiredjobs'),
    path('applications_summary/',views.ApplicationSummary.as_view(),name='summary'),
    path('processapplication/<int:id>',views.ProcessApplication.as_view(),name='process_application'),
    path('change_password/', PasswordChangeView.as_view(template_name='change_password.html',success_url=reverse_lazy('password_changedone'),form_class=MyPasswordchangeForm),name='password_change'),
    path('change_password/done/',PasswordChangeDoneView.as_view(template_name='password_changedone.html'),name='password_changedone')




]