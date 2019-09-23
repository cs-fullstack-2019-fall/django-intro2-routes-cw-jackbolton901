from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("try gogetthegood")

def goods(request):
    return HttpResponse("Here you go! Literally Bare Naked Ladies! ")
def happy(request):
    return HttpResponse("Ren and Stimpy rock")