from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import SignUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.core.mail import send_mail


# Create your views here , for homepage.
def home(request):
    return render(request, 'home/home.html')


# create your views here, for sign up page.
def sign_up(request):
    if request.method == 'POST':
      fm = SignUpForm(request.POST)
      if fm.is_valid():
          messages.success(request, 'Account Created Successfully !!')
          fm.save()
          return redirect('/login/') 
    else:
        fm = SignUpForm()

    return render(request,'home/signup.html', {'form':fm})

# create your views here, for sign up page.
def user_login(request):
     if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            # checking user enter data are valid or not 
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                # authenticate user password and username
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logedin Successfully !!")
                    return HttpResponseRedirect('/')
                else:
                    messages.error(request, "Sorry we can't login in your account")
        else:
            fm = AuthenticationForm()
        return render(request, 'home/user_login.html', {'form':fm})
     else:
         return HttpResponseRedirect('/')



# user profile view function
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
                if fm.is_valid():
                    fm.save()
                    messages.success(request, "Profile Updated Succeffully !!")
                    return render(request, 'home/admin.html', {'name':request.user.first_name, 'form':fm})
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)
                if fm.is_valid():
                    fm.save()
                    messages.success(request, "Profile Updated Succeffully !!")
        else:
            # checking user or admin 
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                return render(request, 'home/admin.html', {'name':request.user.first_name, 'form':fm})
            else:
                fm = EditUserProfileForm(instance=request.user)
        return render(request, 'home/UserProfile.html', {'name':request.user.first_name, 'form':fm})   
    else:
        return HttpResponseRedirect('/login/')



# logout view function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# change password using old password , view function
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, "Password Changed Successfully !!")
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'home/changepass.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')


# contact view function   
def user_contact(request):
    if request.method == 'POST':
            # name = request.POST.get('full-name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            send_mail(
                subject,
                message,
                email,
                ['ajaychaudhari6768@gmail.com'],
                fail_silently=False
            )
            messages.info(request, "Message Send Successfully !! ")
    else:
         return render(request, 'home/contact.html')


# about us view functions 
def aboutUs(request):
    return render(request, 'home/aboutUs.html')





# Education section view functions
# career after 10th
def after10th(request):
    if request.user.is_authenticated:
        return render(request, 'home/after10th.html')
    else:
        return HttpResponseRedirect('/login/')

# career after 12th
def after12th(request):
    if request.user.is_authenticated:
        return render(request, 'home/after12th.html')
    else:
        return HttpResponseRedirect('/login/')

# career after graduation
def aftergraduation(request):
    if request.user.is_authenticated:
        return render(request, 'home/aftergraduation.html')
    else:
        return HttpResponseRedirect('/login/')

def givetestinfo(request):
    if request.user.is_authenticated:
        return render(request, 'home/givetestinfo.html')
    else:
        return HttpResponseRedirect('/login/')

# def footer(request):
#     return render(request,'home/footer.html')