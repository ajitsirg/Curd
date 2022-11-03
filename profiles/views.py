from django.shortcuts import render
from django.http import HttpResponse
from .models import Coustmer

def index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'index.html',context=my_dict) 


def register(request):
    if request.method == "POST":
         name= request.POST['name']
         age= request.POST['age']
         phone= request.POST['phone']
         email= request.POST['email']
         address= request.POST['address']
         city= request.POST['city']
         state= request.POST['state']
         country= request.POST['country']
    
         obj=Coustmer(name=name, age=age, phone=phone, email=email,address=address, city=city, state=state, country=country)
    
         obj.save()
         return HttpResponse("submission successfully registered")
    else:
     return render(request,'register.html')
 
    
    
    
def login(request):
    if request.method == "POST":
        phone =request.POST['phone']
        age =request.POST['age']
        
        obj=Coustmer.objects.filter(phone=phone,age=age)
        
        if obj.exists() :
            return render(request,'dashboard.html')
        else:
           return HttpResponse("login again") 
       
    return render(request,'login.html')        


def dashbord(request):
    data = Coustmer.objects.all().first
    context = {"data": data}
    return render(request,'dashboard.html',context)        
        



          