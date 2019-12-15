from django.shortcuts import render
from django.http import HttpResponseRedirect


def jscode(request):
    return render(request, 'JSCode.html')

def second(request):
    return render(request, '2.html')

def third(request):
    return render(request, '3.html')

def fourth(request):
    return render(request, '4.html')

def fifth(request):
    return render(request, '5.html')
