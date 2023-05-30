from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
#FlashMessage
from django.contrib import messages
from .forms import todoCreateForm,todoUpdateForm

def detail(request,todo_id):

#dictionary | list | array
 TodoID = Todo.objects.get(id=todo_id)
 return render(request,'detail.html',{"todoID":TodoID})

def home(request):

#dictionary | list | array
 all = Todo.objects.all()
 return render(request,'home.html',{"Todos":all})

def delete(request,todo_id):

  Todo.objects.get(id=todo_id).delete()
  messages.success(request,'todo deleted susccessfully', extra_tags='success')
  return redirect('home')

def create(request):

 #method Post
  if request.method == 'POST':

#mehtod post form ro baram biar
    form = todoCreateForm(request.POST)

    if form.is_valid():

        cd = form.cleaned_data
        Todo.objects.create(Name=cd['Name'],Text=cd['Text'],DateTime=cd['DateTime'])
        messages.success(request,'todo created susccessfully', extra_tags='success')

        return redirect('home')

 #method Get
  else:

#mehtod get form ro baram biar
   form = todoCreateForm()
  return render(request,'forms.html',{'form':form})


def update(request, todo_id):


  todo = Todo.objects.get(id=todo_id)

 #method Post
  if request.method == 'POST':

#mehtod post form ro baram biar
    form = todoUpdateForm(request.POST,instance=todo)

    if form.is_valid():

        form.save()
        messages.success(request,'todo updated susccessfully', extra_tags='success')
        return redirect('details',todo_id)

 #method Get
  else:
    
#mehtod get form ro baram biar
   form = todoUpdateForm(instance=todo)
  return render(request,'update.html',{'form':form})