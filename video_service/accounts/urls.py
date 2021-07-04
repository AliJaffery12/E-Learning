
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='accounts'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('signup/',views.registerPage.as_view(),name="signup"),
    path('student/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('teacher/', views.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='reset_password'),
    path('reset_password_done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_complete'),


   
    
    
     

]

