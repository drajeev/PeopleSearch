from django import forms
from people.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        exclude=()
