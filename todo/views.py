from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todoitem
# Create your views here.
def todoView(request):
    todo_item = todoitem.objects.all()
    return render(request,'index.html',{'all_item':todo_item})

def todoadd(request):
    new = todoitem(content = request.POST['content'])
    new.save()
    return HttpResponseRedirect('/todo/')

def tododelete(request,todo_id):
    item = todoitem.objects.get(id = todo_id)
    item.delete()
    return HttpResponseRedirect('/todo/')
    