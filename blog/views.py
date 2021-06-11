from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from.models import Category
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse
from .forms import SimpleForm


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

class SimpleFormView(FormView):
    #specify the form you want use
    form_class = SimpleForm
    #specify name of template
    template_name = 'simpleform.html'
    #specify success url
    success_url = '/categories'

def welcome(request):
    context = {
        'name': 'Linda',
        'email': 'lindaatieno24@gmail.com'
    }
         
    return render(request, "welcome.html",context)

def posts(request):

    context= {}
    
    return render(request, 'blog/post_list.html',context)
