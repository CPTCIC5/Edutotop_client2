from django.shortcuts import  redirect, render
from django.contrib import messages
from .models import Course, Notes,NotesComment,Video,VideoComment
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from  django.contrib.auth.models import User
from django.db.models import F,Q


def index(request):
    qset1=Notes.objects.all().order_by('-published_on')
    course_query=Course.objects.all().order_by('-course_published_on')
    return render(request,'index/home.html',{'qset1':qset1,'course_query':course_query})


@login_required
def notes_upload(request):
    if request.method=='POST':
        title=request.POST.get('title')
        subject=request.POST.get('subject')
        desc=request.POST.get('desc')
        thumbnail=request.FILES.get('thumbnail')
        file=request.FILES['file']
        author=request.user
        if Notes.objects.filter(title=title).exists():
            messages.error(request,'Title Taken')
            return HttpResponseRedirect(reverse('home:notes_upload'))
        elif len(title) > 60:
            messages.info(request,'title too long')
            return render(request,'index/notes_upload.html')
        print(title,thumbnail)
        entry=Notes(title=title,subject=subject,desc=desc,thumbnail=thumbnail,file=file,author=author,published_on=datetime.datetime.now())
        entry.save()
        messages.info(request,'Notes updated successfully!')
        return HttpResponseRedirect('/')
    return render(request,'index/notes_upload.html')

def notes_paginated_view(request,notes_title):
    qset2=Notes.objects.filter(title=notes_title)
    qset3=Notes.objects.get(title=notes_title)
    recommend=Notes.objects.all().order_by('-published_on')[:3]
    if request.method == 'POST':
        message=request.POST.get('message')
        entry=NotesComment(note=qset3,message=message,author=request.user)
        entry.save()
        messages.success(request,'Comment Added Successfully!')
        return render(request,'index/paginated_notes.html',{'qset2':qset2,'qset3':qset3,'recommend':recommend})
    return render(request,'index/paginated_notes.html',{'qset2':qset2,'qset3':qset3,'recommend':recommend})

@login_required
def notes_delete(request,note_title):
    if request.method =='GET' :
        qset3=Notes.objects.get(title=note_title)
        if request.user == qset3.author:
            qset3.delete()
            messages.success(request,'DELETED')
            return HttpResponseRedirect(reverse('home:index'))
    return HttpResponseRedirect(reverse('home:index'))

def search(request):
    if request.method == 'POST':
        searched=request.POST.get('searched')
        if len(searched)>55:
            messages.info(request,'TEXT IS TOO LONG')
            return HttpResponseRedirect(reverse('index:home'))
        q1=Notes.objects.filter(title__contains=searched)
        return render(request,'index/search-result.html',{'q1':q1,'searched':searched})
    return render(request,'index/search-result.html')

def course_paginated_view(request,course_title):
    course_query=Course.objects.filter(course_title=course_title)
    video_query=Course.objects.get(course_title=course_title)
    return render(request,'index/paginated_course.html',{'course_query':course_query,'video_query':video_query})

def bag(request):
    return render(request,'index/bag.html')

def status(request):
    return render(request,'index/status.html')

@login_required
def analytics(request):
    recent=User.objects.get(username=request.user)
    return render(request,'index/analytics.html',{'recent':recent})


def video_paginated_view(request,vid_title):
    qset4=Video.objects.filter(vid_title=vid_title)
    qset5=Video.objects.get(vid_title=vid_title)
    qset5.vid_views = F('vid_views') +1
    qset5.save()
    if request.method == 'POST':
        comment_vid_message=request.POST.get('comment_vid_message')
        entry=VideoComment(video=qset5,comment_vid_message=comment_vid_message,comment_vid_author=request.user)
        entry.save()
        messages.success(request,'Comment Added Successfully!')
        return render(request,'index/paginated_video.html',{'qset4':qset4,'qset5':qset5})
    return render(request,'index/paginated_video.html',{'qset4':qset4,'qset5':qset5})

@login_required
def video_upload(request):
    if request.method == 'POST':
        vid_of=request.POST.get('vid_of')
        course=Course.objects.get(course_title=vid_of)
        print(course)
        vid_title=request.POST.get('vid_title')
        vid_desc=request.POST.get('vid_desc')
        vid_thumbnail=request.FILES.get('vid_thumbnail')
        vid_video=request.FILES['vid_video']
        vid_author=request.user
        if Video.objects.filter(vid_title=vid_title).exists():
            messages.error(request,'Title taken!')
            return render(request,'index/video-upload.html')
        elif len(vid_title)>55:
            messages.error(request,'Title too long!')
            return render(request,'index/video-upload.html')
        entryy=Video(vid_of=course,vid_title=vid_title,vid_desc=vid_desc,vid_thumbnail=vid_thumbnail,vid_video=vid_video,vid_author=vid_author)
        entryy.save()
        messages.success(request,'VID ADDED SUCCESSFULLY')
        return HttpResponseRedirect(reverse('home:index'))
    return render(request,'index/video-upload.html')

@login_required
def video_delete(request,vid_id):
    qset5=Video.objects.get(id=vid_id)
    if request.method == 'GET':
        if request.user == qset5.vid_author:
            messages.success(request,'DELETED')
            qset5.delete()
            return HttpResponseRedirect(reverse('home:index'))
    return HttpResponseRedirect(reverse('home:index'))


@login_required
def course_upload(request):
    if request.method == 'POST':
        course_title = request.POST.get('course_title')
        course_desc = request.POST.get('course_desc')
        course_subj = request.POST.get('course_subj')
        course_thumbnail = request.FILES.get('course_thumbnail')
        print(course_thumbnail)
        course_author = request.user
        if Course.objects.filter(course_title=course_title).exists():
            messages.success(request,'Title taken!')
            return render(request,'index/course-upload.html')
        elif len(course_title)>50:
            messages.error(request,'Title too long!')
            return render(request,'index/course-upload.html')
        entry=Course(course_title=course_title,course_desc=course_desc,course_subj=course_subj,course_thumbnail=course_thumbnail,course_author=course_author)
        entry.save()
        messages.success(request,'Course Uploaded!')
        return HttpResponseRedirect(reverse('home:index'))
    return render(request,'index/course-upload.html')


@login_required
def course_delete(request,course_qset):
    if request.method == 'GET':
        course_qset=Course.objects.get(course_title=course_qset)
        if request.user == course_qset.course_author:
            course_qset.delete()
            messages.success(request,'Course Deleted')
            return HttpResponseRedirect(reverse('home:index'))
    return render(HttpResponseRedirect(reverse('home:index')))