from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDo
# Create your views here.

def list_todo_items (request):
    context = { 'todo_list': ToDo.objects.all() }
    return render(request, 'todos/todo_list.html', context)

def add_item (request: HttpResponse):
    new_conent = ToDo(content = request.POST['content'])
    new_conent.save()
    return redirect('/todos/list/')

def delete_item (request: HttpResponse, todo_id):
    delete_conent = ToDo.objects.get(id = todo_id)
    delete_conent.delete()
    return redirect('/todos/list/')