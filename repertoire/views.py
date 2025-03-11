from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_repertoire(request):
   return HttpResponse("Here will be your repertoire")
