from django.contrib import admin
from django.urls import path,include
from . import views
app_name = "sahamapp"

urlpatterns = [
    path("",views.homePage,name='index'),
    path("FreelancerRegister",views.registerFreelancer,name="registerFL"),
    path("FreelancerLogin", views.loginFreelancer,name='loginFL'),
    path("FreeLancerEdit/<str:freelancerId>", views.editpage,name='editFL'),
    path('FreeLancerAddService/<str:freelancerId>', views.addService,name='addServiceFL'),
    path("DeleteService/<str:serviceId>" , views.deleteService,name='deleteService'),
    path("EditService/<str:serviceId>" , views.editService, name='editService')
]
