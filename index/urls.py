from django.urls import path
from . import views
from django.conf .urls.static import static
from django.conf import settings

app_name='home'

urlpatterns = [
    path('',views.index,name='index'),
    path('notes-upload/',views.notes_upload,name='notes-upload'),
    path('search/',views.search,name='search'),
    path('notes/<str:notes_title>/',views.notes_paginated_view,name='notes_paginated_view'),
    path('notes-delete/<str:note_title>/',views.notes_delete,name='notes-delete'),


    path('course-upload/',views.course_upload,name='course-upload'),
    path('course/<str:course_title>/',views.course_paginated_view,name='course_paginated_view'),
    path('course-delete/<str:course_qset>',views.course_delete,name='course-delete'),

    path('video-upload/',views.video_upload,name='video-upload'),
    path('video/<str:vid_title>/',views.video_paginated_view,name='video_paginated_view'),
    path('video-delete/<int:vid_id>/',views.video_delete,name='video-delete'),

    path('bag/',views.bag,name='bag'),
    path('status/',views.status,name='status'),
    path('analytics/',views.analytics,name='analytics'),
]
urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT) 
