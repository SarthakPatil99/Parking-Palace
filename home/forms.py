from django import forms
from .models import Users
  
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = Users
#         fields = (
#             'user_id', 'user_fname', 'user_mname', 'user_lname', 'user_email', 'user_phone', 'user_pass', 
#             'user_isPO', 'user_Pname', 'user_PAname', 'user_Paddr', 'user_Pimage'
#         )