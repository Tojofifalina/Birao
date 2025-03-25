from django import forms
from Fitatanana.models import Fanamarihana
class FanamarihanaForm(forms.ModelForm):
    class Meta:
        model = Fanamarihana
        fields = ['Fanamarihana','Lohanteny']