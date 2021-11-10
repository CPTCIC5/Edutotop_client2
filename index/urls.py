from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('',views.index,name='index'),
    path('notes/',views.notes,name='notes'),
    path('notes-upload/',views.notes_upload,name='notes_upload'),
    path('notes-search/',views.notes_search,name='notes_search'),
    path('notes/<str:notes_title>/',views.notes_paginated_view,name='notes_paginated_view'),
    path('notes-delete/<str:note_title>/',views.notes_delete,name='notes_delete'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('bag/',views.bag,name='bag')

]