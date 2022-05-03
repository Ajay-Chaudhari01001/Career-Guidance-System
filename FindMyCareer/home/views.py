from django.shortcuts import render

# Create your views here , for homepage.
def home(request):
    return render(request, 'home/home.html')

# create your views here, for sign up page.
def sign_up(request):
    return render(request,'home/signup.html')

# create your views here, for sign up page.
def login(request):
    return render(request, 'home/login.html')