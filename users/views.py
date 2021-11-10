from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile,Contact
from django.core.exceptions import ValidationError
from django.urls import reverse
import datetime

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
                messages.success(request,'Account Created!')
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
def profile(request):
    queryset=Profile.objects.filter(user=request.user)
    queryset2=User.objects.all()
    return render(request,'users/profile.html',{'queryset':queryset,'queryset2':queryset2})

@login_required
def profile_create(request): 
    if request.method=='POST':
        try:
            user=request.user
            image=request.FILES.get('image')
            about=request.POST.get('about')
        except ValidationError:
            messages.error(request,'ADD IMG TYPE OF FILE')
            return render(request,'profile_create.html')
        if len(about)>200:
            messages.info(request,'ABOUT IS TOO LONG')
            return render(request,'index/profile_create.html')
        data=Profile(user=user,image=image,about=about)
        data.save()
        messages.success(request,'Profile created')
        return HttpResponseRedirect(reverse('users:profile'))
    return render(request,'users/profile_create.html')
