from django.shortcuts import render
from django.http import HttpResponse
from.models import Category
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse


# Create your views here.

def home(request):

    #dictionary with initial data
    #with field name as keys

    context = {}

    #add dictionary during initiliasation

    context["categories"]= Category.objects.all()[:2]
    return render(request,"home.html",context)

class MyView(View):

    def get(self,request):
      return HttpResponse('My first class based view')    

class CategoryList(ListView):

    model = Category

class CategoryDetail(DetailView):

    model = Category

class CategoryCreate(CreateView):  
    model = Category

    #specify the fields to be displayed

    fields = ['name']

    #function to ridirect user

    def get_success_url(self):
        return reverse('category_list')

class CategoryUpdate(UpdateView):

    model = Category
    fields = ['name'] 
    success_url = '/categories'

class CategoryDelete(DeleteView):

    model = Category
    success_url = '/categories'