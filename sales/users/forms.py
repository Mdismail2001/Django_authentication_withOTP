from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email'] 
        if commit:
            user.save()
        return user
 

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))



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
