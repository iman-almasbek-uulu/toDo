from django.http import request
from django.shortcuts import render, HttpResponse



def homepage(request):
    return HttpResponse("hello iman")


def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("my name is Iman!")

