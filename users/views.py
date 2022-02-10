from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile,Contact
from django.urls import reverse
import datetime
from django.contrib.auth import logout as auth_logout
from .forms import ProfileForm

def settings(request):
    return render(request,'users/settings.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return render(request,'users/signup.html')
            elif len(password) <8:
                messages.info(request,'ATLEAST 8 CHARACTER PASSWORD NEEDED')
                return render(request,'users/signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return render(request,'users/signup.html')
            else:
                entry=User.objects.create_user(username=username,email=email,password=password)
                entry.save()
                return HttpResponseRedirect(reverse('users:login'))
        else:
            messages.info(request,'Password and confirm password didn"t match')
    return render(request,'users/signup.html')


@login_required
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        number=request.POST.get('number')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contacted_on=datetime.datetime.now()
        contacted_by=request.user
        contact_entry=Contact(name=name,number=number,email=email,message=message,contacted_on=contacted_on,contacted_by=contacted_by)
        contact_entry.save()
        messages.success(request,'THANKS FOR CONTACTING US! WE WILL REACH TO U ASAP')
        return HttpResponseRedirect(reverse('home:index'))
    return render(request,'users/contact.html')

@login_required
def profile(request,id):
    queryset=Profile.objects.filter(user=id)
    queryset2=Profile.objects.get(user=id)
    return render(request,'users/profile.html',{'queryset':queryset,'queryset2':queryset2})


@login_required
def profile_update(request,id):
    queryset_update=Profile.objects.get(user=id)
    form = ProfileForm(request.POST or None, instance = queryset_update)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('users:profile'))
    return render(request,'users/profile_update.html',{'queryset_update':queryset_update,'form':form})


def logout(request):
    auth_logout(request)
    messages.success(request,'Logout Successful')
    return HttpResponseRedirect(reverse('home:index'))
