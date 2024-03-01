
from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('innerpage/', views.inner, name='inner'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('upload/', views.upload, name='upload'),
    path('details/', views.details, name='details'),
    path('users/', views.user, name='users'),
    path('adminhome/', views.adminhome, name='adminhome'),




]
