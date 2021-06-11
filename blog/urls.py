from django.urls import path
from . import views
from blog.views import CategoryDelete, CategoryUpdate, MyView,CategoryList,CategoryDetail ,CategoryCreate, SimpleFormView



urlpatterns=[
    path("", views.home, name='home'),
    path('view/',MyView.as_view()),
    path('categories/',CategoryList.as_view(),name="category_list"),
    path('category/detail/<pk>',CategoryDetail.as_view(),name= 'category_detail'),
    path('create/category', CategoryCreate.as_view(),name= 'category_create'),
    path('update/category/<pk>/',CategoryUpdate.as_view(),name='category_update'),
    path('delete/category/<pk>/',CategoryDelete.as_view(),name='category_delete'),
    path('simple/form', SimpleFormView.as_view(),name='simpleform'),
    path('welcome',views.welcome, name='welcome'),
    path('posts', views.posts , name="posts" )

]