from django.urls import path,re_path
from urllib import request
from . import views
from .models import Subject

app_name='courses'
urlpatterns=[

    
    #path('',CourseList.as_view(),name='course_list'),
    
    #path('<slug>', views.CourseDetailView.as_view(), name='course_detail'),
    #re_path('<slug:create>/',views.CreateCourseView.as_view(),name='Create_course'),
    #re_path('<slug:section>/',views.AddSectionsView.as_view(),name='AddSection'),
    path('',views.Homepage.as_view(),name="course_list"),
    path('lessoncreate/',views.mytutorial,name="lesson"),
    path("<single_slug>", views.single_slug, name="single_slug"),
    path('create/',views.courseCreate,name="course_create"),
    path('subjectcreate/',views.SubjectCreate,name="Addsubject"),
    path('Cart/',views.MyCoursesCart,name='Cart'),
    path('search/',views.Search,name='search'),
    path('relatedQuizes/<int:quiz_id>/',views.QuizSelectrelated,name='relate'),
   
    
   
   
    
    #path('subjectlists/',SectionsListView.as_view(),name='SectionsList'),
   
   
    
    
    
   

]