from django.urls import path
from . import views
from blog.views import CategoryDelete, CategoryUpdate, MyView,CategoryList,CategoryDetail ,CategoryCreate, SimpleFormView
from blog.views import PostDelete, PostUpdate, PostList, PostDetail,PostCreate
from blog.views import FeedbackDelete, FeedbackUpdate, FeedbackList, FeedbackDetail,FeedbackCreate
from blog.views import TagDelete, TagUpdate, TagList, TagDetail,TagCreate



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
    path('update/post/<pk>/',PostUpdate.as_view(),name='post_update'),
    path('delete/post/<pk>/',PostDelete.as_view(),name='post_delete'),
    path('posts/',PostList.as_view(),name='posts'),
    path('create/post',PostCreate.as_view(),name='post_create'),
    path('detail/post/<pk>/',PostDetail.as_view(),name='post_detail'),
    path('update/feedback/<pk>/',FeedbackUpdate.as_view(),name='feedback_update'),
    path('delete/feedback/<pk>/',FeedbackDelete.as_view(),name='feedback_delete'),
    path('feedback/',FeedbackList.as_view(),name='feedback_list'),
    path('create/feedback',FeedbackCreate.as_view(),name='feedback_create'),
    path('detail/feedback/<pk>/',FeedbackDetail.as_view(),name='feedback_detail'),
    path('update/tag/<pk>/',TagUpdate.as_view(),name='tag_update'),
    path('delete/tag/<pk>/',TagDelete.as_view(),name='tag_delete'),
    path('tag/',TagList.as_view(),name='tag_list'),
    path('create/tag',TagCreate.as_view(),name='tag_create'),
    path('detail/tag/<pk>/',TagDetail.as_view(),name='tag_detail'),
    path('model/form/category',views.formCategory),
    path('add/form/comment',views.add_comment),




]