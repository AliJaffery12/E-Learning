from django.db import models
from courses.models import Subject
# Create your models here.
# Create your models here.
class Quiz(models.Model):
    quiz_title = models.CharField(max_length=300)
    slug=models.SlugField(blank=True)
    num_questions = models.IntegerField(default=0)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.quiz_title

    @staticmethod
    def get_all_Quiz_by_subjectid(subject_id):
        if subject_id:
            return Quiz.objects.filter(subject=subject_id)
        else:
            return Quiz.objects.all();
         
    

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300)
    question_num = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
