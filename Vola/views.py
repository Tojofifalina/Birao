from django.shortcuts import render
from .form import FampidiraMbola,FamoahaMbola
from django.shortcuts import render, get_object_or_404,redirect
# Create your views here.
def Vola_Niditra(request):
    if request.method == 'POST':
        form = FampidiraMbola(request.POST)
        if form.is_valid():
            form.save()
        return redirect("Vola:Vola_Niditra")
    else:
        form = FampidiraMbola()

    context = {"form": form, }
    return render(request,'vola/Ampiditra_vola.html',context)

def Vola_Nivoka(request):
    if request.method == 'POST':
        form = FamoahaMbola(request.POST)
        if form.is_valid():
            form.save()
        return redirect("Vola:Vola_Nivoka")
    else:
        form = FamoahaMbola()

    context = {"form": form, }
    return render(request,'vola/FamoahaMbola.html',context)