from django.shortcuts import render,redirect
from trial_app.models import Users
# Create your views here.
from django.http import HttpResponse
def admission(request):
    return render(request,'home.html')


def registerUser(request):
    user = Users()
    print(request.POST.get("name"))
    user.name = request.POST.get("name")
    user.email = request.POST.get("email")
    user.address = request.POST.get("address")
    user.gender = request.POST.get("gender")
    # user.hobbies = request.POST.get("hobbies[]")
    hobby = ','.join(request.POST.getlist("hobbies[]"))
    print(hobby)
    user.hobbies = hobby
    user.city = request.POST.get("cities")
    user.dob = request.POST.get("birthday")
    user.password = request.POST.get("psw")
    user.confirm_password = request.POST.get("psw-repeat")
    user.save()
    response = HttpResponse("Success")
    return redirect("/readUsers")


def readUsers(request):
    data = Users.objects.all()
    print(data)
    return render(request,'index.html',{"data":data})

def deleteUsers(request,id):
    dat = Users.objects.get(id=id)
    dat.delete()
    return redirect("/readUsers")

def editUsers(request,id):
    dat = Users.objects.get(id=id)
    hobbies1 = dat.hobbies
    hobbies = set(hobbies1.split(","))
    games = {"cricket","football","hockey"}
    rem_games = games.difference(hobbies)
    hobbies = hobbies1.split(",")
    rem_games = list(rem_games)
    cities = ["mumbai","pune","delhi"]
    print(dat.dob)
    date = dat.dob
    return render(request,"edit.html",{"data":dat,"hobbies":hobbies,"remaining_games":rem_games,"cities":cities, 'date':date})

def updateUser(request,id):
    user = Users.objects.get(id=id)
    user.name = request.POST.get("name")
    user.email = request.POST.get("email")
    user.address = request.POST.get("address")
    user.gender = request.POST.get("gender")
    # user.hobbies = request.POST.get("hobbies[]")
    hobby = ','.join(request.POST.getlist("hobbies[]"))
    print(hobby)
    user.hobbies = hobby
    user.city = request.POST.get("cities")
    user.dob = request.POST.get("birthday")
    user.password = request.POST.get("psw")
    user.confirm_password = "dummy"
    user.save()
    response = HttpResponse("Success")
    return redirect("/readUsers")