from django.shortcuts import render, HttpResponseRedirect


# Education section view functions
# career after 10th
def after10th(request):
    if request.user.is_authenticated:
        return render(request, 'educards/after10th.html')
    else:
        return HttpResponseRedirect('/login/')

# career after 12th
def after12th(request):
    if request.user.is_authenticated:
        return render(request, 'educards/after12th.html')
    else:
        return HttpResponseRedirect('/login/')

# career after graduation
def aftergraduation(request):
    if request.user.is_authenticated:
        return render(request, 'educards/aftergraduation.html')
    else:
        return HttpResponseRedirect('/login/')

# def footer(request):
#     return render(request,'educards/footer.html')