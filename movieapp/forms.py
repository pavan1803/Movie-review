from django import forms 
from django.contrib.auth.models import User
from movieapp.models import UserDetails


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model =User
        fields = ['username','email','password']

class UserProfile(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['phone','age','userpic']


