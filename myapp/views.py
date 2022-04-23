from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import  userprofile
from .forms import profile,loginform
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

def register(request):
    if request.method=="POST":
        # print(request.POST)
        if userprofile.objects.filter(email=request.POST['email']):
            messages.warning(request, "Email already linked with another account. Kindly login")
            return redirect('login')
        form=profile(request.POST)
        if form.is_valid():
            # User.objects.create_user
            obj=User.objects.create_user(username=request.POST["email"],
                                         password=request.POST["password"],
                                         email=request.POST["email"])
            obj.save()
            userprofile(user=obj,
                        firstname=request.POST["firstname"],
                        lastname=request.POST["lastname"],
                        email=request.POST["email"],
                        phonenumber=request.POST["phonenumber_0"]+request.POST["phonenumber_1"],
                        country=request.POST["country"],
                        password=request.POST["password"]
                        ).save()
            # form.save()
            return redirect('login')
    else:
        form=profile()
    return render(request,'myapp/register.html',{'form':form})


def loginf(request):
    if request.method=="POST":
        # print(request.POST)
        if not userprofile.objects.filter(email=request.POST['email']):
            messages.success(request, "Account does not exist. Create new account")
            return redirect('register')
        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        # print(user)
        if user is not None:
            login(request, user)
            # messages.success(request, f'Welcome to Centum World!')
            # print(request.user)
            return redirect('dash')
        else:
            messages.success(request, "Give correct Deatils")
            return redirect('login')
    else:
        form=loginform()
    return render(request,'myapp/login.html',{'form':form})


@login_required
def dash(request):
    if request.user.is_authenticated:
        obj = userprofile.objects.get(user=request.user)
        getu=userprofile.objects.all().filter(email=request.user).values()
        getu=[i for i in getu]
    # print(getu)
    # u[0]["email"]
    # print(getu[0])
    else:
        # messages.success(request,"Kindly Login First!")
        return redirect('login')
    return render(request,'myapp/dash.html',{"getu":getu[0],"date":datetime.datetime.now()})

def logoutf(request):
    logout(request)
    return redirect('login')