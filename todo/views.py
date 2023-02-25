from datetime import datetime
from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm, CheckboxForm
import json

@csrf_protect
def set_todo_info(req):
    form = TodoForm(req.POST)
    checkbox = CheckboxForm(req.POST)
    todos = Todo.objects.values()
    context = {
        'form': form,
        'checkbox': checkbox,
        'todos': todos
    }


    if req.method == 'POST':
        title = req.POST['title']
        desc = req.POST['description']
        Todo.objects.create(
            title=title,
            description=desc
        )
        return redirect('/')
    else:
        return render(req, 'index.html', context)


@csrf_protect    
def update_todo_status(request, id):
    req_query_set = Todo.objects.filter(pk=id)
    stringify_Json = serialize('json', req_query_set)
    dic_json = json.loads(stringify_Json)
    db_isDone_status = dic_json[0]['fields']['isDone']
    
    try:
        a = Todo.objects.get(pk=id)
        a.isDone = not db_isDone_status
        a.save()
    finally:
        return redirect('/')
