from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1> This is Homepage </h1> <a href='contact/'>Contact | <a href='/about/'> About </a> ")
def contact(request):
    return HttpResponse("<h1> This is Contact  </h1> <a href='/'>Home Page | <a href='/about/'> About </a>")
def about(request):
    return HttpResponse("<h1> This is About </h1> <a href='/'>Home Page | <a href='/contact/'> Contact Page </a>")