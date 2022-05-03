from django.contrib.auth import logout
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login 

# Create your views here.

def home(request):
    return render(request, 'home.html')

def loginUser(request):
    if request.method=="POST":
         uname = request.POST.get('uname')
         password1 = request.POST.get('password1')
         
        
    else:
        return render(request, 'login.html')
    # check if user has entered correct credentials
    user = authenticate(username=uname, password=password1)
    print(user)
    
    if user is not None:
        # A backend authenticated the credentials
        login(request,user)
        return render(request,"dashboard.html")
    else:
        # No backend authenticated the credentials
        messages.error(request, 'Invalid Credentials !')
        return render(request, 'login.html')
    


    


def logoutUser(request):
    logout(request)
    return redirect("home")