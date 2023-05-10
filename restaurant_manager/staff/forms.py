from django import forms
from django.forms import ModelForm # Line 2, "forms.py"
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('name', 'email', 'phone', 'address','position', 'salary')


#from django import forms
#from .models import Staff

#class StaffForm(forms.ModelForm):
 #   class Meta:
  #      model = Staff
   #     fields = ('name', 'email', 'phone_number', 'address', 'position', 'salary')
