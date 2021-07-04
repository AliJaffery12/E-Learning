from django.db import models
from django.urls import reverse
from memberships.models import Membership
from memberships.models import UserMembership
from django.utils.text import slugify
from accounts.models import User
from datetime import datetime
# Create your models here.
class Course(models.Model):
    #course_id = models.IntegerField(primary_key=True)
    course_slug= models.CharField(max_length=200,default=1)
    title= models.CharField(max_length=264)
    description = models.TextField(max_length=500)
    thumbnail= models.ImageField(blank=True,null=True)
    allowed_memberships= models.ManyToManyField(Membership)
    
    class Meta:
        verbose_name_plural="Courses"

    


    def __str__(self):
        return self.title
    '''@property
    def image_url(self):
        """
        Return self.photo.url if self.photo is not None, 
        'url' exist and has a value, else, return None.
         """
        if self.thumbnail:
            return getattr(self.thumbnail, 'url', None)
        return None'''

    @staticmethod
    def get_course_by_id(ids):
        return Course.objects.filter(id__in=ids)
    
    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')


    def get_absolute_url(self):
        return reverse('courses:course_detail', kwargs={'slug': self.slug})


class Subject(models.Model):
    #subject_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    course= models.ForeignKey(Course,default=1,verbose_name="Course",on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    description = models.TextField(max_length=500,blank=True)


    class Meta:
        verbose_name_plural="Subjects"


    def __str__(self):
        return self.name

   
    def get_absolute_url(self):
        return reverse('courses:subject_detail',args=[self.id,])

    @staticmethod
    def get_all_subjects():
        return Subject.objects.all()
    

class Lesson(models.Model):
    
    Lesson_title= models.CharField(max_length=264)
    video_url= models.FileField(upload_to='images/',blank=True)
    subject=models.ForeignKey(Subject, default=1,verbose_name="Subject",on_delete=models.CASCADE)
    #created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    #created_at = models.DateTimeField(auto_now_add=True)
    tutorial_published = models.DateTimeField("date published", default=datetime.now(),blank=True)
    position = models.IntegerField()
    Lesson_slug=models.CharField(max_length=200,default=1)

    
    

    def __str__(self):
        return self.Lesson_title
    

    
    


    