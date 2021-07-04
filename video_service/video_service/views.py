from django.views.generic import TemplateView
from courses.models import Course
from django.contrib import messages
from django.shortcuts import render
#from django.core.email import send_mail
class TestPage(TemplateView):
    template_name= 'quiz/test.html'



class ThanksPage(TemplateView):
    template_name= 'quiz/thanks.html'
    

def Homepage(request):
    return render(request,template_name='courses/index.html')

def Contactpage(request):
    if request.method=="POST":
        message_name=request.POST['msg-name']
        message_email=request.POST['msg-email']
        subject=request.POST['msg-subject']
        message=request.POST['msg-txt']

        send_mail(
            message_name,
            subject,
            message_email,
            message,
            ['17221598-025@uog.edu.pk']

        )

        return render(request,template_name='courses/contact.html')
    else:

        return render(request,template_name='courses/contact.html')
    
def Search(request):
    query=request.GET['query']
    if len(query)>70:
        allcourses=Course.objects.none()
    else:

        allcoursesTitle=Course.objects.filter(title__icontains=query)
        alldescriptionAdd=Course.objects.filter(description__icontains=query)
        allcourses=allcoursesTitle.union(alldescriptionAdd)
    if allcourses.count()==0:
        messages.error(request,"No Result Found Plz refine your Search")
    params={'allcourses':allcourses,'query':query}
    return render(request,'courses/SearchCourse.html',params)

def AboutPage(request):
    return render(request,template_name='courses/about.html')