from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('detail', views.task_detail, name="task_detail"),
    path('detail/<str:pk>', views.single_task_detail, name="single_task_detail"),
    path('create', views.single_task_create, name="single_task_create"),
    path('modify/<str:pk>', views.single_task_modify, name="single_task_modify"),
    path('delete/<str:pk>', views.single_task_delete, name="single_task_delete")

]
