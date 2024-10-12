from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    username = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))


class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6, widget= forms.TextInput(attrs={'placeholder': 'OTP'}))
    
    

class ProfileForm(forms.ModelForm):
     class Meta:
         model = Profile
         fields =['mobile_number', 'address', 'website']
         widgets = {
             'mobile_number': forms.TextInput(attrs={'placeholder': 'Mobile Number'}),
             'address': forms.Textarea(attrs={'placehole': 'Address', 'rows': 3}),
             'website': forms.TextInput(attrs={'placeholder': 'Website'})
             
         }
