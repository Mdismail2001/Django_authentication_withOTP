from django.shortcuts import render, redirect, HttpResponse
from .forms import LoginForm, OTPForm, ProfileForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
import random
from .models import UserOTP, Profile
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})





def login_view(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form = LoginForm(request.POST, data = request.POST)  
        if form.is_valid():
            user = form.get_user()  
            
            otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            user_otp, created = UserOTP.objects.get_or_create(user=user)           
            user_otp.otp = otp
            user_otp.save()            
            print(f"OTP for {user.username}:{otp}")
            request.session['pre_otp_user_id'] = user.id
            
            return redirect('otp_view')
            # if user is None:
            #     return redirect('login')  
            
            # login(request, user) 
            # return redirect('home')  
    
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home_view(request):
    return render(request, 'home.html')


def otp_view(request):
    user_id = request.session['pre_otp_user_id']
    if not user_id:
        return redirect('login')
    user = User.objects.get(id = user_id)
    user_otp = UserOTP.objects.get(user=user)
    if request.method =="POST":
        form = OTPForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data.get('otp')
            if otp == user_otp.otp:
                user_otp.otp = ''
                user_otp.save()
                login(request,user)
                del request.session['pre_otp_user_id']
                return render(request, 'home/index.html')
            else:
                form.add_error('otp', 'Invalid OTP')
    else:
        form = OTPForm()
    return render(request, 'otp.html', {'form': form})


@login_required
def profile_update(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_update')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'home/page-user.html', {'form': form})



def tabile_list(requset):
    return render(requset, 'home/ui-tables.html')


def typography_views(request):
    return render(request,'home/ui-typography.html')



def icon_views(request):
    return render(request, 'home/ui-icons.html')


def maps_views(request):
    return render(request, 'home/ui-maps.html')


def notifications_views(request):
    return render(request, 'home/ui-notifications.html')


def rtl_support_views(request):
    return render(request, 'home/page-rtl-support.html')