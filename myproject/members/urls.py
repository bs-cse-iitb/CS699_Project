from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('registration/addrecord/', views.addrecord, name='addrecord'),
    #path('generateotp/', views.generateotp, name='generateotp'),
    path('verifyemailreq/', views.verifyemailreq, name='verifyemail'),
    path('verifyemailreq/verifyemail/', views.verifyemail, name='verifyemail'),
    path('login/', views.login, name='login'),
    path('loginverify/', views.loginverify, name='loginverify'),
    

]