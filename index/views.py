from django.shortcuts import  redirect, render
from django.contrib import messages
from .models import Notes#,Video
from datetime import datetime
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime


def index(request):
    qset1=Notes.objects.all()
    return render(request,'index/home.html',{'qset1':qset1})

def notes(request):
    note=Notes.objects.all()
    return render(request,'index/notes.html',{'note':note})


def dashboard(request):
    return render(request,'users/dashboard.html')

@login_required
def notes_upload(request):
    if request.method=='POST':
        try:
            title=request.POST.get('title')
            subject=request.POST.get('subject')
            desc=request.POST.get('desc')
            thumbnail=request.FILES.get('thumbnail')
            file=request.FILES['file']
            author=request.user
        except ValidationError:
            messages.error(request,'ADD PDF FILE')
            return render(request,'index/notes_upload.html')
        if Notes.objects.filter(title=title).exists():
            messages.error(request,'Title Taken')
            return HttpResponseRedirect(reverse('home:notes_upload'))
        elif len(title) > 60:
            messages.info(request,'title too long')
            return render(request,'index/notes_upload.html')
        elif len(subject) > 60:
            messages.info(request,'subject too long')
            return render(request,'index/notes_upload.html')
        else:
            entry=Notes(title=title,subject=subject,desc=desc,thumbnail=thumbnail,file=file,author=author,published_on=datetime.now())
            entry.save()
            messages.info(request,'Notes updated successfully!')
            return HttpResponseRedirect('/')
    return render(request,'index/notes_upload.html')

def notes_paginated_view(request,notes_title):
    qset2=Notes.objects.filter(title=notes_title)
    return render(request,'index/paginated_notes.html',{'qset2':qset2})

@login_required
def notes_delete(request,note_title):
    if request.method =='GET':
        qset3=Notes.objects.filter(title=note_title).delete()
        messages.success(request,'DELETED')
        return HttpResponseRedirect(reverse('home:index'))
    return HttpResponseRedirect(reverse('home:index'))

def notes_search(request):
    if request.method == 'POST':
        searched=request.POST.get('searched')
        if len(searched)>55:
            messages.info(request,'TEXT IS TOO LONG')
            return render(request,'index/notes.html')
        q1=Notes.objects.filter(title__contains=searched)
        return render(request,'index/notes_search.html',{'q1':q1,'searched':searched})
    return render(request,'index/notes.html')

def bag(request):
    return render(request,'index/bag.html')

"""
@login_required
def video_upload(request):
    if request.method == 'POST':
        vid_title=request.POST.get('vid_title')
        vid_subject=request.POST.get('vid_subject')
        vid_desc=request.POST.get('vid_desc')
        vid_thumbnail=request.FILES.get('vid_thumbnail')
        vid_video=request.FILES['vid_video']
        vid_author=request.user
        vid_published_on=datetime.datetime.now()
        if ValidationError:
            messages.error(request,'PLZ SELECT PARTICULAR FILE FORMAT')
            return render(request,'index/video_upload.html')
        if ValueError:
            pass
        entryy=Video(vid_title=vid_title,vid_subject=vid_subject,vid_desc=vid_desc,vid_thumbnail=vid_thumbnail,vid_video=vid_video,vid_author=vid_author,vid_published_on=vid_published_on)
        entryy.save()
        messages.success(request,'VID ADDED SUCCESSFULLY')
        return HttpResponseRedirect(reverse('home:index'))
    return render(request,'index/video_upload.html')

def watch_video(request,vid_id):
    qset4=Video.objects.filter(id=vid_id)
    qset4.vid_views=+1
    return render(request,'index/paginated_video.html',{'qset4':qset4})

@login_required
def video_delete(request,vid_id):
    if request.method == 'GET':
        qset5=Video.objects.filter(id=vid_id).delete()
        messages.success(request,'DELETED')
        return HttpResponseRedirect(reverse('home:index'))
    return HttpResponseRedirect(reverse('home:index'))
"""