from django.urls import path,reverse_lazy
from Candidate import views
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from Employer.forms import MyPasswordchangeForm

urlpatterns = [
    path('home', views.CandidateHome.as_view(), name='c_home'),
    path('joblist', views.JoblistView.as_view(), name='c_joblist'),
    path('jobdetail/<int:id>', views.JobdetailView.as_view(), name='c_jobdetail'),
    path('addprofile', views.AddprofileView.as_view(), name='c_profile'),
    path('viewprofile/', views.ProfileView.as_view(), name='c_viewprofile'),
    path('editprofile/<int:id>', views.EditprofileView.as_view(), name='c_editprofile'),
    path('jobapply/<int:id>', views.JobapplyView.as_view(), name='c_jobapply'),
    path('appliedjobs', views.AppliedJobsView.as_view(), name='c_appliedjobs'),
    path('search', views.JobSearchView, name='c_search'),
    path('change_password/', PasswordChangeView.as_view(template_name='c_change_password.html',
                                                              success_url=reverse_lazy('c_password_changedone'),
                                                              form_class=MyPasswordchangeForm), name='c_password_change'),
    path('change_password/done/', PasswordChangeDoneView.as_view(template_name='c_password_changedone.html'),
         name='c_password_changedone'),
    path('notifications',views.NotificationView.as_view(),name='notification')

]
