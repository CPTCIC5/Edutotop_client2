from django.contrib import admin
from .models import Notes,Video,Course,NotesComment,VideoComment

admin.site.register(Video)
admin.site.register(Notes)
admin.site.register(Course)
admin.site.register(NotesComment)
admin.site.register(VideoComment)
