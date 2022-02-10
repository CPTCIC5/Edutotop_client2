from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='users'

urlpatterns = [
    path('settings/',views.settings,name='settings'),
    path('register/',views.register,name='register'),
    path('contact/',views.contact,name='contact'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('profile/<int:id>/',views.profile,name='profile'),
    path('profile-update/<int:id>',views.profile_update,name='profile_update'),
    path('logout/',views.logout,name='logout')
]