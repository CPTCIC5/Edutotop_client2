from django.contrib.messages.api import debug
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import validate_image_file_extension
from django.dispatch import receiver 
from django.db.models.signals import post_save


class Profile (models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    about=models.CharField(max_length=200,blank=True)
    image=models.ImageField(default='default.jpeg',upload_to='Profile_Pics',blank=True,null=True,validators=[validate_image_file_extension])


    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        
        instance.profile.save()
    
    def save(self,*args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300 or img.height < 300 or img.width < 300 :
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        verbose_name_plural='Profile'

class Contact(models.Model):
    name=models.CharField(max_length=60,null=False,blank=False)
    number=models.CharField(max_length=12)
    email=models.EmailField(max_length=70)
    message=models.TextField(null=False,blank=False)
    contacted_on=models.DateTimeField(auto_now_add=True)
    contacted_by=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}-{self.contacted_on}"