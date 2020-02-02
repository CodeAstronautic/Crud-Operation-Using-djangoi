from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname','emp_code','mobile','position')
#def __init__(self,*args,**kwargs):
     #super(EmployeeForm,self).__init__(*args,**kwargs) 
     #self.fields['position'.empty_label]     