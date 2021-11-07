from django.urls import path
from . import views

app_name = 'ToDo' #  do linkow w html trzeba dodawac ta nazwe

urlpatterns = [
    #widoki posta
    path('', views.task_list, name='task_list'), #pierwszy '' oznacza ze nie pobieramy zadnych argumentow
    path('change_status/<int:pk>/', views.change_status, name='change_status'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    path('mark_all_done', views.mark_all_done, name='mark_all_done'),
    path('delete_all', views.delete_all, name='delete_all'),

]