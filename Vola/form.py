from django import forms
from .models import VolaNiditra,VolaNivoka

class FampidiraMbola(forms.ModelForm):
    class Meta:
        model = VolaNiditra
        fields= ["Taona","Daty","Antony","Vola","Fanamarihana"]
class FamoahaMbola(forms.ModelForm):
    class Meta:
        model = VolaNivoka
        fields= ["Taona","Daty","Antony","Vola","Fanamarihana"]