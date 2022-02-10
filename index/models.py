from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator,validate_image_file_extension
from PIL import Image


subject_choices={
    ("Maths","Maths"),
    ("Physics","Physics"),
    ("Chemistry","Chemistry")
}

class Notes(models.Model):
    title=models.CharField(max_length=60,blank=False,null=False,unique=True)
    subject=models.CharField(max_length=50,choices=subject_choices,null=False,blank=False)
    desc=models.TextField(blank=True,null=False,default='No desc')
    thumbnail=models.ImageField(default='default_notes.jpeg',upload_to='thumbnail_notes',validators=[validate_image_file_extension])
    file=models.FileField(blank=False,null=False,upload_to='Notes',validators=[FileExtensionValidator(allowed_extensions=['pdf','doc','docx'])])
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    published_on=models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)

    def __str__(self):
        return  self.title
    
    
    def save(self):
        super().save()

        img = Image.open(self.thumbnail.path)

        if img.height > 300 or img.width > 300:
            output_size = (290, 163)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)
    
    class Meta:
        verbose_name_plural='Notes'


class NotesComment(models.Model):
    note=models.ForeignKey(Notes,on_delete=models.CASCADE)
    message=models.CharField(max_length=100,null=False,blank=False)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    commented_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.note)



course_subject_choices={
    ("Maths","Maths"),
    ("Physics","Physics"),
    ("Chemistry","Chemistry")
}

class Course(models.Model):
    course_title=models.CharField(max_length=90,unique=True,null=False,blank=False)
    course_desc=models.TextField(null=False,blank=False)
    course_subj=models.CharField(max_length=20,choices=course_subject_choices,blank=False,null=False)
    course_thumbnail=models.ImageField(upload_to='Course_Thumbnail',default='default_course.jpeg',validators=[validate_image_file_extension])
    course_author=models.ForeignKey(User,on_delete=models.CASCADE)
    course_published_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_title

    def save(self):
        super().save()

        img = Image.open(self.course_thumbnail.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.course_thumbnail.path)



class Video(models.Model):
    vid_of=models.ForeignKey(Course,on_delete=models.CASCADE)
    vid_title=models.CharField(max_length=60,blank=False,null=False,unique=True)
    vid_desc=models.TextField(blank=True,null=False,default='no desc')
    vid_thumbnail=models.ImageField(default='default_video.png',upload_to='thumbnail_video',validators=[validate_image_file_extension])
    vid_video=models.FileField(blank=False,null=False,upload_to='Videos',validators=[FileExtensionValidator(allowed_extensions=['mp4','MOV','WMV','AVI','AVCHD','FLV', 'F4V','SWF','MKV'])])
    vid_author=models.ForeignKey(User,on_delete=models.CASCADE)
    vid_published_on=models.DateTimeField(auto_now_add=True)
    vid_views=models.IntegerField(default=0)
    vid_likes=models.IntegerField(default=0)
    vid_dislikes=models.IntegerField(default=0)

    def __str__(self):
        return self.vid_title

    def save(self):
        super().save()

        img = Image.open(self.vid_thumbnail.path)

        if img.height > 300 or img.width > 300 or img.height < 300 or img.width < 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.vid_thumbnail.path)

class VideoComment(models.Model):
    video=models.ForeignKey(Video,on_delete=models.CASCADE)
    comment_vid_message=models.CharField(max_length=100,null=False,blank=False)
    comment_vid_author=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_vid_commented_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.video)
