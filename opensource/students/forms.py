

from django import forms



class StudentForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age =forms.IntegerField()
    email = forms.EmailField()
    image = forms.CharField()
    gender = forms.ChoiceField(choices=[('m', 'Male'), ('f', 'Female')])
    salary = forms.IntegerField()


    # add validation to your form