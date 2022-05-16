from django.shortcuts import render
from .models import GuessCareer
# Create your views here.

def question_form(request):
    data = GuessCareer.objects.all()
    return render (request, 'predict/qaform.html', {'key':data})

# Here we have created a function called ' 
# question_form' in which we have declared a variable named 'data' 
# and we stored the all objects of the database in this variable. By using this variable as a key we 
# can use this into any html page.