from django import forms
from .models import Mpino3,Adidy,Katekomen,Fanamarihana
from datetime import date
from django.core.exceptions import ValidationError
#------------------------------------------------------------------------------------------------------------------------
"""
    Mety Miasa 
"""
class Mombamoba2(forms.ModelForm):
    class Meta:
        model = Mpino3
        fields= ["LaharanaKaratra","Anarana","Fanampiny","Teraka",
                 "L_v","Antonasa","Adresy","Faritra","Fiday","TaonaNahatogavanaTaoAmpiagonana",
                 "FiagonanaNiavina","batisa","taona_nanaovana_batysa","M_P","TaonaNahaMpandray","DatyNakanaKaratra"]

        label = {"Laharan'ny Karatra","Anarana","Fanampiny","Teraka","Toherana Nahaterahana",
                 "Lahy/Vavy","Antonasa","Adresy","Faritra","Fiday","Taona Nahatogavana Tao Ampiagonana",
                 "Fiagonana Niavina","batisa","Taona nanaovana batisa","Mpandray/Kristianina","Taona Naha Mpandray","Daty NakanaKaratra"}
    L_v = forms.ChoiceField(choices=Mpino3.l_v,widget=forms.RadioSelect)
    batisa = forms.ChoiceField(choices=Mpino3.b_t, widget=forms.RadioSelect)
    M_P = forms.ChoiceField(choices=Mpino3.m_p, widget=forms.RadioSelect)

    def clean(self):
        cleaned_data = super().clean()
        anarana = cleaned_data.get('Anarana')
        fanampiny = cleaned_data.get('Fanampiny')
        LaharanaKaratra = cleaned_data.get('LaharanaKaratra')

        """
        if Mpino3.objects.filter(Anarana=anarana, Fanampiny=fanampiny,LaharanaKaratra=LaharanaKaratra).exists():
            raise forms.ValidationError("Efa misy")
        """
        return cleaned_data


class ApiditraAdidy(forms.ModelForm):
    class Meta:
        model = Adidy
        fields = ["Mpino","Taona","J","P_J","J_Date","F","P_F","F_Date","M","P_M","M_Date","Av","P_Av","Av_Date",
                  "Ma","P_Ma","Ma_Date","Ji","P_Ji","Ji_Date","Ju","P_Ju","Ju_Date","Ag","P_Ag","Ag_Date","S","P_S","S_Date","Ak","P_Ak","Ac_Date",
                  "N","P_N","N_Date","D","P_D","D_Date"]
    def clean(self):
        cleaned_data = super().clean()
        taona = cleaned_data.get('Taona')
        mpino = cleaned_data.get('Mpino')
        Pj = cleaned_data.get('P_J')

        M_p = cleaned_data.get('P_M')

        diovina = ['P_J', 'P_F', 'P_M', 'P_Av',
                   'P_Ma', 'P_Ji', 'P_Ju', 'P_Ag', 'P_S', 'P_Ak',
                   'P_N', 'P_D', "P_N"]
        if Adidy.objects.filter(Taona=taona, Mpino=mpino).exists():
            raise forms.ValidationError("Efa misy")

        elif M_p == "K":
            print("dfsfdfsdfs")
            for volana in diovina:
                v = cleaned_data(volana)
                if v is not None and v !=0:
                    raise forms.ValidationError("Tsy mbola pandray io olona io")
        return cleaned_data





class ApiditraAdidyMisy(forms.ModelForm):
    class Meta:
        model = Adidy
        fields = ["Mpino","Taona","J","P_J","J_Date","F","P_F","F_Date","M","P_M","M_Date","Av","P_Av","Av_Date",
                  "Ma","P_Ma","Ma_Date","Ji","P_Ji","Ji_Date","Ju","P_Ju","Ju_Date","Ag","P_Ag","Ag_Date","S","P_S","S_Date","Ak","P_Ak","Ac_Date",
                  "N","P_N","N_Date","D","P_D","D_Date"]

    """
    def clean_J(self):
        j = self.cleaned_data.get('J')

        if self.instance and self.instance.pk:
            if self.instance.J > 0:
                if j != self.instance.J:
                    raise forms.ValidationError("Tsy azo ovaina")
        return j"""

    def clean(self):
        cleaned_data = super().clean()

        diovina = ['Taona','J','P_J','F','P_F','M','P_M','Av','P_Av',
                  'Ma','P_Ma','Ji','P_Ji','Ju','P_Ju','Ag','P_Ag','S','P_S','Ak','P_Ak',
                  'N','P_N','D','P_D']

        for field in diovina:
            miditra = cleaned_data.get(field)
            efamisy = getattr(self.instance,field,None)
            taona = cleaned_data.get('Taona')
            if efamisy is not None and efamisy > 0 and miditra != efamisy:
                raise forms.ValidationError(f"Tsy azo ovaina io fa efa misy: {field.upper()}")

        return cleaned_data
"""
class AmpiditraKatekomen(forms.ModelForm):
    class Meta:
        model = Katekomen
        fields = ["Mpino","Taompianarana","Daty_Nidirana"]
"""
class AmpiditraKatekomen(forms.Form):
    Anarana = forms.CharField(max_length=100, required=False, label="Anarana")
    Fanampiny = forms.CharField(max_length=100, required=False, label="Fanampiny")
    Karatra = forms.CharField(max_length=10, required=False, label="Karatra")
    Taona = forms.IntegerField(label="Taona", min_value=1900, max_value=date.today().year)
    Daty_Nidirana = forms.DateField(label="Daty_Nidirana", widget=forms.DateInput(attrs={'type': 'date'}))

    def clean(self):
        cleaned_data = super().clean()
        Anarana = cleaned_data.get('Anarana')
        Fanampiny = cleaned_data.get('Fanampiny')
        Karatra = cleaned_data.get('Karatra')

        # Valider que soit nom/prénom soit code d'identification est fourni
        if not (Anarana and Fanampiny) and not Karatra:
            raise ValidationError("Mila Anarana na Famampin'Ananarana na Laharan'ny Karatra.")

        # Vérifier si une personne correspond
        from .models import Mpino3
        mpino = None

        if Karatra:
            try:
                mpino = Mpino3.objects.get(LaharanaKaratra=Karatra)
            except Mpino3.DoesNotExist:
                raise ValidationError("Tsy ao anatin'ireo Mpino io Laharana Karatra io.")
        elif Anarana and Fanampiny:
            try:
                mpino = Mpino3.objects.get(Anarana=Anarana, Fanampiny=Fanampiny)
            except Mpino3.DoesNotExist:
                raise ValidationError("Tsy misy Mpino manana io Anarana io.")
        elif Karatra and Anarana and Fanampiny:
            try:
                mpino = Mpino3.objects.get(Anarana=Anarana, Fanampiny=Fanampiny, LaharanaKaratra=Karatra)
            except Mpino3.DoesNotExist:
                raise ValidationError("Tsy misy Mpino manana io Anarana ,Fanampiny sy Laharana Karatra io .")
        # Vérifier si la personne possède déjà un compte
        from .models import Katekomen
        if Katekomen.objects.filter(Mpino__LaharanaKaratra=Karatra).exists():
            raise ValidationError("Efa Misy.")

        cleaned_data['mpino'] = mpino  # Ajouter la personne validée au formulaire
        return cleaned_data

class AnovaKatekomen(forms.ModelForm):
    class Meta:
        model = Katekomen
        fields = ['Taompianarana', 'Daty_Nidirana']
        widgets = {
            'Daty_Nidirana': forms.DateInput(attrs={'type': 'date'}),
        }

