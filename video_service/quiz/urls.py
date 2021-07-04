from django.urls import path

from . import views


app_name = 'quiz'
urlpatterns = [
    # ex: /quiz/
    path('', views.index, name='index'),
    #path("quiz_slug", views.single_slug, name="quiz_slug"),

    # ex: /quiz/5/
    path('<int:quiz_id>/', views.single_quiz, name='single_quiz'),

    # ex: /quiz/5/3/
    path('<int:quiz_id>/<int:question_id>/', views.single_question, name='single_question'),

    # ex: /quiz/5/3/vote/
    path('<int:quiz_id>/<int:question_id>/vote/', views.vote, name='vote'),

    # ex: /quiz/5/results/
    path('<int:quiz_id>/results/', views.results, name='results'),

    # ex: /quiz/create/
    path('create/', views.create_quiz, name='create_quiz'),

    # ex: /quiz/create/7/2/
    path('create/<int:quiz_id>/<int:question_id>/', views.create_question, name='create_question'),
    path('certificate/',views.render_pdf_view,name='get_certificate'),
    path('courselist/',views.CourseListView,name='course_Listview'),
    path('pdf/<pk>/',views.student_course_pdf,name='student_certificate'),
    
   

]