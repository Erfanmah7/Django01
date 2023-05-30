#namayesh dar templates
from django.shortcuts import render,redirect
#namayesh sadeh
from django.http import HttpResponse
#forms
from . import forms
#register
from django.contrib.auth.models import User
#login logout authenticate(user,pass)
from django.contrib.auth import authenticate,login,logout
#flash messages
from django.contrib import messages

def user_register(request):

    if request.method == 'POST':

       form = forms.userRegisterForm(request.POST)

       if form.is_valid():

            cd = form.cleaned_data
            user =  User.objects.create_user(username=cd['username'],email=cd['email'],password=cd['password'])
            user.firstname = cd['firstname']
            user.lastname = cd['lastname']
            user.save()
            messages.success(request,'is register','success')
            return redirect('home')

    else:

       form = forms.userRegisterForm()

    return render(request,'register.html',{'form':form})


def user_login(request):
    
   if request.method == 'POST':
    
      form = forms.userLoginForm(request.POST)
      
      if form.is_valid():

         cd = form.cleaned_data
         user = authenticate(request,username=cd['username'],password=cd['password'])

         if user is not None:

            login(request,user)
            messages.success(request,'is login','success')
            return redirect('home')

         else:

               messages.error(request,'is not login','danger')

   else:
    
      form = forms.userLoginForm()

   return render(request,'login.html',{'form':form})


def user_logout(request):
    
   logout(request)

   messages.success(request,'is logout','success')

   return redirect('home')