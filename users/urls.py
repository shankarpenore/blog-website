from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='index'),
    path('register/',views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login_user'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout_user'),
    path('update/',views.update, name='update'),
    path('profile/',views.profile, name='profile'),
]