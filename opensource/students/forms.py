

from django import forms

from departments.models import Department
from students.models import Student


class StudentForm(forms.Form):
    """ each field defined in the form class, translate to html elements ? label , input , error """
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age =forms.IntegerField()
    email = forms.EmailField()
    image = forms.CharField()
    gender = forms.ChoiceField(choices=[('m', 'Male'), ('f', 'Female')])
    salary = forms.IntegerField()
    department = forms.ModelChoiceField(queryset=Department.objects.all())


    # add validation to your form
    # you can define validation rules you need ?
    def clean_email(self):
        email = self.cleaned_data['email']
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email


    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters")
        return name



# automatically create form based on model structure
class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters")
        return name

