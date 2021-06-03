"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from blog.views import CategoryDelete, CategoryUpdate, MyView,CategoryList,CategoryDetail ,CategoryCreate


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('blog.urls')),
    path('view/',MyView.as_view()),
    path('categories/',CategoryList.as_view(),name="category_list"),
    path('category/detail/<pk>',CategoryDetail.as_view(),name= 'category_detail'),
    path('create/category', CategoryCreate.as_view(),name= 'category_create'),
    path('update/category/<pk>/',CategoryUpdate.as_view(),name='category_update'),
    path('delete/category/<pk>/',CategoryDelete.as_view(),name='category_delete')



]

