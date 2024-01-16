from django import forms
from .models import Customers
from django.core.exceptions import ValidationError

class SignupForm(forms.Form): 
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat your password'}))

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        new = Customers.objects.filter(cemail=email)
        if new.exists():
            raise ValidationError("Email Already Exists")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        return password

    def clean_re_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password != re_password:
            raise ValidationError("Passwords do not match")

    def save(self):
        customer = Customers.objects.create(cemail=self.cleaned_data['email'], cpassword=self.cleaned_data['password'], cname=self.cleaned_data['name'])
        return customer
    