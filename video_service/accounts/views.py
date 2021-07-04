#from django.shortcuts import render

# Create your views here.
from . import forms
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.forms import inlineformset_factory
#from django.views.generic import CreateView
# Create your views here.
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from .decorators import student_required,teacher_required
from .forms import  StudentSignUpForm,TeacherSignUpForm
from .models import User,Student,Teacher
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from django.contrib.auth.forms import UserCreationForm



class registerPage(TemplateView):
    #form_class=forms.UserCreateForm
    #
    success_url=reverse_lazy('student_signup')
    template_name="accounts/signup.html"

    

    
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:login')






class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:login')

