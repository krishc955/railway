from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
    # return HttpResponse("this is home page")  

def service(request):
    return render(request, 'service.html')
   # return HttpResponse("this is service page")

def login(request):
    return render(request, 'login.html')
   # return HttpResponse("this is login page")

def signup(request):
    return render(request, 'signup.html')
   # return HttpResponse("this is login page")