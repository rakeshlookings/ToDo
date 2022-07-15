from django.urls import path,include
from . import views

urlpatterns = [
    path('list/', views.list_todo_items),
    
    path('add-item/', views.add_item, name = 'insert_todo_item'),

    path('delete-todo/<int:todo_id>/',views.delete_item,name='delete_todo_item'),
]