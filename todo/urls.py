from django.urls import path
from . import views

urlpatterns = [
    path('', views.set_todo_info, name='set_todo'),
    path('update-todo-status/<int:id>', views.update_todo_status, name='update_status')
]