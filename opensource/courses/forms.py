from courses.models import Course
from django import forms


class CourseForm(forms.ModelForm):
    notes =forms.CharField(max_length=100)
    class Meta:
        model = Course
        fields = '__all__'


    