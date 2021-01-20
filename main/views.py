from django.shortcuts import render, HttpResponse
from .models import ToDo

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")

def hw_31(request):
    return render(request, "hw_31.html")

def hw_31_1(request):
    return render(request, "hw_31_1.html")

def hw_31_2(request):
    return render(request, "hw_31_2.html")