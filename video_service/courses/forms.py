from django import forms


from courses.models import Course,Subject,Lesson

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'


class AddSectionForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields='__all__'


class AddLessonForm(forms.ModelForm):
    class Meta:
        model=Lesson
        fields='__all__'




