from django import forms  
from django.forms.fields import EmailField  
from django.forms.forms import Form  
  
class LoginForm(forms.Form):
    cemail = forms.EmailField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    cpassword = forms.CharField(max_length=100, min_length=8, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)
