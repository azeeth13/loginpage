from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from datetime import datetime
from .models import User


hozir=datetime.now()

ismlar=['Azizbek','Azamat',"Temur","Jasmin"]

def HomePage(request):
    return render(request,'in1dex.html',{"Time" :hozir})


def AboutPage(request,id=4):
    users=User.objects.all()
    return render(request, 'about.html',{"users":users})


def Contactpage(request):
    if request.method=="POST":
        
        ism=request.POST.get('ism')
        familya=request.POST.get("familya")
        yosh=request.POST.get("yosh")
        email=request.POST.get("email")
        User.objects.create(first_name=ism,last_name=familya,age=yosh,email=email)
        return redirect('about')
        print("ism",ism,"familya",familya,"yosh",yosh,"email", email)
    return render(request,'contact.html')


def UpdataePage(request,id):
    person=User.objects.get(id=id)
    if request.method=="POST":
        person.first_name=request.POST.get('ism')
        person.last_name=request.POST.get("familya")
        person.age=request.POST.get("yosh")
        person.email=request.POST.get("email")
        person.save()
        return redirect('about')
    return render(request,'update.html')

# def (request,id):
#     person=User.objects.get(id=id)
#     person.delete()
#     return redirect('about')

def index(request): 
    people = User.objects.all() 
    return render (request, "index.html", ( {"people": people})) 
    
def create(request): 
    if request.method == "POST": 
        klient = User() 
        klient.name = request.POST.get("name") 
        klient.age = request.POST.get("age") 
        klient. save () 
        return HttpResponseRedirect("/") 
        # изменение данных в БД 
def edit(request, id): 
    try: 
        person = User.objects.get(id=id) 
        if request.method == "POST": 
            person.name = request.POST.get("name") 
            person.age = request.POST.get("age") 
            person. save () 
            return HttpResponseRedirect("/") 

        else: 
            return render(request, "edit.html", {"person": person}) 
    except: 
     return HttpResponseNotFound("<h2>Foydalanuvchi idsi mavjud emas</h2>")

def DeletePage(request, id): 
    try: 
        person = User.objects.get(id=id) 
        person.delete() 
        return HttpResponseRedirect("/") 
    except:
        return redirect('about')
# def DeletePage(request)