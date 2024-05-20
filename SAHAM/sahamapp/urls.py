from django.contrib import admin
from django.urls import path,include
from . import views
app_name = "sahamapp"

urlpatterns = [
    path("",views.homePage, name='index'),
    path("FreelancerRegister",views.registerFreelancer, name="registerFL"),
    path("FreelancerLogin", views.loginFreelancer, name='loginFL'),
    path("FreeLancerEdit/<str:freelancerId>", views.editpage, name='editFL'),
    path('FreeLancerAddService/<str:freelancerId>', views.addService, name='addServiceFL'),
    path("DeleteService/<str:serviceId>" , views.deleteService, name='deleteService'),
    path("EditService/<str:serviceId>" , views.editService, name='editService'),
    path("CustomerLogin", views.loginCustomer, name='loginC'),
    path("CustomerRegister",views.registerCustomer, name="registerC"),
    path("FavoriteServices/<str:customerId>", views.editpage, name='favoriteServices'),
    path("ShowService/<str:username>/<str:serviceId>" , views.showService, name='showService'),
    path("ShowServices/<str:username>", views.showServices, name='showServices'),
    path("BookService/<str:username>/<str:serviceId>" , views.showService, name='bookService'),
    path("BookedServices/<str:username>", views.bookedServices, name='bookedServices')
]