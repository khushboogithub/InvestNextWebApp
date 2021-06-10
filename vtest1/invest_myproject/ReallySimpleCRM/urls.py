from django.urls import path

from . import views

urlpatterns = [
    path('', views.landingPage, name='index'),
    path('landingPage', views.landingPage, name='landingPage'),
    path('home', views.home,name='home'),
    path('loginPage', views.loginPage,name='loginPage'),
    path('register', views.register,name='register'),
    path('addContacts', views.addContacts, name='addContacts'),
    path('deleteContact', views.deleteContact, name='deleteContact'),
    path('logout', views.logout, name='logout'),

]
