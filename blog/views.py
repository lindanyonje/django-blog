from django.shortcuts import render
from django.http import HttpResponse
from.models import Category

# Create your views here.

def home(request):

    #dictionary with initial data
    #with field name as keys

    context = {}

    #add dictionary during initiliasation

    context["dataset"]= Category.objects.all()
    return render(request,"home.html",context)
