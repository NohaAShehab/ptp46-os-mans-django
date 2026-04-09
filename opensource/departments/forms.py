

from django import forms

from departments.models import Department


class DepartmentForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    logo = forms.ImageField()
    active = forms.BooleanField()

    def clean_name(self):
        name = self.cleaned_data['name']
        if Department.objects.filter(name=name).exists():
            raise forms.ValidationError("Department with this name already exists")
        return name
