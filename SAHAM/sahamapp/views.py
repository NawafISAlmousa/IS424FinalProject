from django.shortcuts import render,HttpResponseRedirect,redirect,reverse, get_object_or_404
from .models import Service,Freelancer,Customer
from django import forms
import random
import string


def generateUniqueIdProvider():
    length = 6
    characters = string.ascii_letters + string.digits
    while True:
        new_id = ''.join(random.choices(characters, k=length))
        if not Freelancer.objects.filter(freelancerId=new_id).exists():
            return new_id
        
def generateUniqueIdService():
    length = 6
    characters = string.ascii_letters + string.digits
    while True:
        new_id = ''.join(random.choices(characters, k=length))
        if not Service.objects.filter(serviceId=new_id).exists():
            return new_id
        
    

def homePage(request):
    return render(request,"sahamapp/index.html")



def registerFreelancer(request):
    if request.method == "POST":
        form = request.POST
        freelancer = Freelancer(freelancerId = generateUniqueIdProvider(),
                                email = form["email"],
                                password = form["password"],
                                description = form["description"],
                                name = form["username"],
                                phonenumber = form["phonenumber"])
        freelancer.save()
        return render(request, 'sahamapp/loginFL.html', {
            'registrationComplete': True
        })
    return render(request,'sahamapp/registerFL.html')


def loginFreelancer(request):
    if request.method == "POST":
        form = request.POST
        current = Freelancer.objects.filter(email = form["email"])
        print(current)
        if current.exists():
            if current[0].password == form["password"]:
                return redirect(reverse('sahamapp:editFL', kwargs={'freelancerId': current[0].freelancerId}))
        return render(request, "sahamapp/loginFL.html",{
            'error':True})   
    return render(request , "sahamapp/loginFL.html")

def editpage(request, freelancerId):
 
 
    freelancer = get_object_or_404(Freelancer, pk=freelancerId)
    services = Service.objects.filter(freelancer=freelancer)
    return render(request, 'sahamapp/editPage.html', {
        'services': services,
        'freelancer': freelancer
    })


def addService(request, freelancerId):
    freelancer = get_object_or_404(Freelancer, pk=freelancerId)
    if request.method == "POST":
        form = request.POST
        Service.objects.create(
            serviceId= generateUniqueIdService(),
            name= form.get("serviceName"),
            description= form.get("serviceDescription"),
            price=form.get("price"),
            freelancer=freelancer)
        return redirect(reverse('sahamapp:editFL', kwargs={"freelancerId":freelancerId}))
    else:
        return render(request, 'sahamapp/addService.html', {'freelancer': freelancer})
    
def deleteService(request, serviceId):
    freelancer = Service.objects.filter(serviceId=serviceId)[0].freelancer
    Service.objects.get(serviceId=serviceId).delete()
    return redirect(reverse('sahamapp:editFL', kwargs={'freelancerId': freelancer.freelancerId}))

def editService(request, serviceId):
    service = Service.objects.filter(serviceId=serviceId)[0]
    if request.method == "POST":
        form = request.POST

        freelancer = Service.objects.filter(serviceId=serviceId)[0].freelancer
        service.name = form.get("serviceName")
        service.description = form.get("serviceDescription")
        service.price=form.get("price")
        service.save()
        return redirect(reverse('sahamapp:editFL', kwargs={'freelancerId': freelancer.freelancerId}))
    return render(request, 'sahamapp/editService.html', {'serviceId': serviceId, 'service':service})


# Customer views

def loginCustomer(request):
    if request.method == "POST":
        form = request.POST
        current = Customer.objects.filter(userName = form["username"])
        if current.exists():
            if current[0].password == form["password"]:
                return redirect(reverse('sahamapp:showServices', kwargs={'username': current[0].userName}))
        return render(request, "sahamapp/loginC.html",{
                'error':True})
    return render(request , "sahamapp/loginC.html")

def registerCustomer(request):
    if request.method == "POST":
        form = request.POST
        existing = Customer.objects.filter(userName = form["username"]).exists()
        if existing :
                    return render(request, 'sahamapp/registerC.html', {
            'UsernameUsed': True
        })
        customer = Customer(userName = form["username"],
                                password = form["password"])
        customer.save()
        return render(request, 'sahamapp/loginC.html', {
            'registrationComplete': True
        })
    return render(request,'sahamapp/registerC.html')

def showServices(request, username):
    services = Service.objects.all()
    return render(request, 'sahamapp/showServices.html', {
        'services': services,
        'username': username
    })
def showService(request, username, serviceId):
    service = Service.objects.filter(serviceId=serviceId)[0]
    if request.method == "POST":
        Customer.objects.get(userName=username).bookedServices.add(service)
        return redirect(reverse('sahamapp:bookedServices', kwargs = {'username': username}))
    return render(request, 'sahamapp/showService.html', {'username': username, 'service':service})

def bookedServices(request, username):
    customer = get_object_or_404(Customer, userName=username)
    services = customer.bookedServices.all()
    return render(request, 'sahamapp/bookedServices.html', {
        'services': services,
        'username': username
    })