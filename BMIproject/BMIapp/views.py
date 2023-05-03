from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "homepage.html" )

def cal(request):
    return render(request, "calculate.html" )

def table(request):
    return render(request, "bmitable.html" )

def history(request):
    return render(request, "history.html" )