from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.work_upload_List.as_view()),
    #path('',views.index),
    path('<int:pk>/', views.PostUpdate.as_view(), name='review_edit'),
    #path('<int:pk>/', views.single_post_page),
    path('search/<str:q>/', views.PostSearch.as_view()),

    path('create_work_upload/', views.PostCreate.as_view()),

    path('<int:pk>/delete/', views.delete_post),

    path('loginout/', include('loginout.urls')),

]