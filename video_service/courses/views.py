from django.shortcuts import render
from memberships.models import UserMembership
from django.urls import reverse_lazy,reverse
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView,DeleteView,FormView,View)
from .models import Course,Lesson,Subject
from quiz.models import Quiz
from .forms import CourseForm,AddSectionForm,AddLessonForm
from django.db.models import Q
from django.contrib import messages
from django.views import View

from django.core.paginator import Paginator

#class CreateCourseView(CreateView):
 #   form_class=CourseForm
  #  #context_object_name='course'
   # slug_field = 'create'
    #slug_kwargs_field='create'
    #model=Course
    #template_name='courses/course_create.html'
   


    # def get_success_url(self):
     #   return reverse_lazy('courses:single_slug')
def courseCreate(request):
    if request.method=="GET":
        form=CourseForm()
        return render(request,"courses/course_create.html",{'form':form})
    else:
        form=CourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/courses')



def SubjectCreate(request):
    if request.method=="GET":
        form=AddSectionForm()
        return render(request,"courses/AddSubjectcategory.html",{'form':form})
    else:
        form=AddSectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/courses')

class Homepage(View):
    def post(self,request):
        mycourse=request.POST.get('mycourse')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(mycourse)
            if quantity:
                cart[mycourse]=quantity+1
            else:
                cart[mycourse]=1

            
        else:
            cart={}
            cart[mycourse]=1
        request.session['cart']=cart
        print( request.session['cart'])
        return redirect('courses:course_list')

    def get(sef,request):
        c_list=Course.objects.all()
        p=Paginator(Course.objects.all(),2)
        page=request.GET.get('page')
        my_paginator=p.get_page(page)
        
        return render(request,template_name='courses/course_lists.html',context={'courses':Course.objects.all(),'my_paginator':my_paginator})

  

def homepage(request):
    return render(request,template_name='courses/course_lists.html',context={'courses':Course.objects.all()})
    # def get_context_data(self, **kwargs):
     #   context = super().get_context_data(**kwargs)
      #  return context

def mytutorial(request):
    if request.method=="GET":
        form=AddLessonForm()
        return render(request,"courses/addvideo.html",{'form':form})
    else:
        form=AddLessonForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/courses')

    #form = AddLessonForm(request.POST,request.FILES)

    #if form.is_valid():
     #   form.save()
     #   return redirect(reverse('courses:course_list'))
   # return render(request, 'courses/addvideo.html', {'form': form})
    #    courses = self.model.objects.all()
     #   return courses


#class CourseDetailView(DetailView):
 #   model=Course
   

#class AddSectionsView(CreateView):
 #   form_class=AddSectionForm
  #  slug_field = 'section'
   # slug_kwargs_field='section'
    #context_object_name='course'
   # model=Subject
    #template_name='courses/Add_Subject.html'


    # def get_success_url(self):
     #   return reverse_lazy('courses:AddSection')

def single_slug(request,single_slug):

    courses=[c.course_slug for c in Course.objects.all()]
    
   
    if single_slug in courses:
        matching_subjects= Subject.objects.filter(course__course_slug=single_slug)
        series_url={}

        for m in matching_subjects.all():

            part_one=Lesson.objects.filter(subject__name= m.name).earliest("tutorial_published")
            series_url[m]=part_one.Lesson_slug
            
        return render(request=request,template_name='courses/category.html',context={"tutorial_series":matching_subjects,"part_ones":series_url})
    

        
    

    tutorials=[t.Lesson_slug for t in Lesson.objects.all()]

    if single_slug in tutorials:
        this_tutorial=Lesson.objects.get(Lesson_slug=single_slug)
        tutorial_from_series=Lesson.objects.filter(subject__name=this_tutorial.subject).order_by("tutorial_published")
        this_tutorial_idx=list(tutorial_from_series).index(this_tutorial)
        
        return render(request=request,template_name='courses/tutorial.html',context={"tutorial":this_tutorial,"sidebar":tutorial_from_series,"this_tutorial_idx":this_tutorial_idx})
    
    



    
#class SectionsListView(ListView):
    
 #   context_object_name='sections'
  #  model=Subject
   # courses=Course.objects.all()

    #queryset = Subject.objects.filter(course__slug=courses.slug)

    #queryset=Subject.objects.filter(course=self.course)
    #template_name='courses/Subject_lists.html'
    

 # def subject_list(request,course_slug=None):


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
    
    

def QuizSelectrelated(request,id):
    sub_quiz=Quiz.objects.select_related('subject').get(pk=id)
    
    return render(request,'quiz/relatedQuizes.html',context={'relateQuiz':sub_quiz})





def MyCoursesCart(request):
    ids=list(request.session.get('cart').keys())
    myCourses=Course.get_course_by_id(ids)
    print(myCourses)
    return render(request,template_name="courses/MyCourses.html",context={'myCourses':myCourses})




class LessonDetailView(View):
    def get(self,request,c_slug,l_slug,*args,**kwargs):
        course_qs=Course.objects.filter(course_slug=c_slug)
        if course_qs.exists():
            course = course_qs.first()

        lesson_qs=course.lessons.filter(Lesson_slug=l_slug)
        if lesson_qs.exists():
            lesson = lesson_qs.first()   

        user_membership=UserMembership.objects.filter(user=request.user).first()
        user_membership_type=user_membership.membership.membership_type
        course_allowed_mem_types= course.allowed_memberships.all()

        context={
            'object': None
        }

        if course_allowed_mem_types.filter(membership_type=user_membership_type).exists():
            context={
                'object':lesson
            }

        return render(request,"courses/category.html",context)