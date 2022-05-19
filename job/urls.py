from django.urls import path,reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView
from job import views
from job.forms import ResetpasswordForm

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.SignupView.as_view(), name='register'),
    path('signin/', views.SigninView.as_view(), name='login'),
    path('signout/', views.SignoutView, name='logout'),
    path('search', views.SearchView.as_view(), name='search'),
    # path('password/',auth_views.PasswordChangeView.as_view(template_name='changepassword.html')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='resetpassword.html'),name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='resetpassword_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='resetpassword_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='resetpassword_complete.html'),name='password_reset_complete'),
    # path('password/',views.ChangePasswordView.as_view(),name='changepassword'),
    # path('success',views.PasswordSuccess,name='success')
]

