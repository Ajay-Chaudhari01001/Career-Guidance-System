from collections import UserDict
from xml.dom import UserDataHandler
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):

    # get the post parameters
    
    if request.method == 'POST':

        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # create the user

        myuser = User.objects.create_user(username, email=username,password=password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " Your Account has been successfully created")
        return redirect('login')
    
    
    return render(request, 'signup.html')