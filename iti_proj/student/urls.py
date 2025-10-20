from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views. student_create, name='student_create'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('details/<int:pk>/', views.student_detail, name='student_detail'),
    path('update/<int:pk>/', views.student_update, name='student_update'),

]
