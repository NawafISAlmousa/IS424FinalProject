from django.shortcuts import render
from .models import Service,Freelancer,Customer
from django import forms
import random
import string


def generate_unique_id():
    length = 6
    characters = string.ascii_letters + string.digits
    while True:
        new_id = ''.join(random.choices(characters, k=length))
        if not Freelancer.objects.filter(freelancerId=new_id).exists():
            return new_id
        
    

def homePage(request):
    return render(request,"sahamapp/index.html")



def registerFreelancer(request):
    if request.method == "POST":
        form = request.POST
        freelancer = Freelancer(freelancerId = generate_unique_id(),
                                email = form["email"],
                                password = form["password"],
                                description = form["description"],
                                name = form["username"],
                                phonenumber = form["phonenumber"])
        freelancer.save()
        return render(request, 'sahamapp/index.html')
        
    # freelancerId = models.CharField(max_length=6,primary_key=True)
    # email = models.EmailField(max_length=256,unique=True)
    # password = models.CharField(max_length=32, validators=[MinLengthValidator(6)])
    # description = models.CharField(max_length=500)
    # name = models.CharField(max_length=32, validators=[MinLengthValidator(3)])
    # phonenumber = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    return render(request,'sahamapp/registerFL.html')


def loginFreelancer(request):
    if request.method == "POST":
        form = request.POST
        current = Freelancer.objects.filter(email = form["email"])
        print(current)
        if current.exists():
            if current[0].password == form["password"]:
                # TEESTING
                return render(request, "sahamapp/index.html")
            return render(request, "sahamapp/loginFL.html",{
                   'error':True
                })
            
        
    return render(request , "sahamapp/loginFL.html")

def editpage(request):
    return render(request ,'sahamapp/editPage.html')