from django.urls import path,include
from . import views
from django_private_chat import urls as django_private_chat_urls

urlpatterns = [
    path('',include('django_private_chat.urls')),

]