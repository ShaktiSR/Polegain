from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('autoadmin/',admin.site.urls),
    path('', views.home, name='home.html'),
    path('create_poll', views.create_poll, name='create_poll'),
    path('home', views.home, name='home'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logout, name='logout'),
    path('regist', views.regist, name='regist'),
    path('daily_poll', views.daily_poll, name='daily_poll'),
    path('user_profile', views.user_profile, name='user_profile'),
    #path('services', views.services, name='services'),
    #path('contect', views.contact, name='contect'),
    path('vote/<poll_id>/', views.vote, name='vote'),
    path('results/<poll_id>/', views.results, name='results'),

]