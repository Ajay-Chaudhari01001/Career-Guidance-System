from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here , for homepage.
def home_page(request):
    return render(request, 'home/home.html')


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
                ['satish8888001591@gmail.com'],
                fail_silently=False
            )
            messages.info(request, "Message Send Successfully !! ")
    else:
         return render(request, 'home/contact.html')


# about us view functions 
def aboutus(request):
    return render(request, 'home/aboutus.html')



# def footer(request):
#     return render(request,'home/footer.html')