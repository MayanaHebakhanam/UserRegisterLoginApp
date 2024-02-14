from django.shortcuts import render,HttpResponse,redirect
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

#@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method =='POST':

          username= request.POST.get('username')
          email= request.POST.get('email')
          password1= request.POST.get('password1')
          password2= request.POST.get('password2')

          if password1!=password2:
               return HttpResponse("Your Password and Confirm password are not same, Please enter correct Password")
          else:
               user_data=User(username=username,email=email,password1=password1,password2=password2)
               user_data.save()
               return redirect("login")

    return render(request,'signup.html')

def LoginPage(request):
    if request.method =='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(request,username=username,password1=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is not correct!")
            
    return render(request,'login.html')



def LogoutPage(request):
    logout(request)
    return redirect('login')