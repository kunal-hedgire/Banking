"""BankingProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BankApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/',views.login),
    path('register/',views.register),
    #path('show/',views.DiffAcc),
    path('details/<int:id>',views.Acc_Register),
    path('info/',views.Acc_Info),
    path('get/',views.Acc_Get),
    path('insurance/',views.Insurance_Info),
    path('loan/',views.Loan_Reg),
    path('with/',views.With_Depo)


]
