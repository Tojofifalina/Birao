from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def anokatra(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("Fitatanana:Pejy1")
        else:
            messages.info(request,"Tsy misokatra")
    form = AuthenticationForm()
    return render(request,"Fanamarinana/Fanamarinana.html",{"form":form})

def anidy(request):
    logout(request)
    return redirect("Fitatanana:Pejy1")
