from django.shortcuts import render

#------------------------------------------------------------------------------------------
from django.http import  HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required,permission_required
from .models import Mpino3,Adidy,Katekomen
from .form import Mombamoba2,ApiditraAdidy,ApiditraAdidyMisy,AmpiditraKatekomen,AnovaKatekomen
from django.db.models import Q

from datetime import date

"""
        Adidy Fiagonana 
"""
def Voloany(request):
    return render(request,'Fiagonana/Pejy1.html')
#@login_required

def Ikaroka(request,code):
    if request.method == 'POST':
        form = Mombamoba2(request.POST)
        if form.is_valid():
            form.save()
        return redirect("Fitatanana:adrana")
    else:
        form = Mombamoba2()
    moba = Mpino3.objects.all()
    fikaroana = request.GET.get('q','')
    if not fikaroana:
        fikaroana = date.year
    ita = Mpino3.objects.filter(Anarana__icontains = fikaroana) or Mpino3.objects.filter( LaharanaKaratra__icontains=str(fikaroana)) if fikaroana else None
    context = {"form":form,"moba":moba,"fikaroana":fikaroana,"ita":ita,"code":code}

    return render(request,'Fiagonana/anova_mobamoba.html',context)
#@login_required
def Adrana(request):
    if request.method == 'POST':
        form = Mombamoba2(request.POST)
        if form.is_valid():

            anarana = form.cleaned_data['Anarana']
            fanampiny = form.cleaned_data['Fanampiny']
            LaharanaKaratra = form.cleaned_data['LaharanaKaratra']

            if Mpino3.objects.filter(Anarana=anarana, Fanampiny=fanampiny, LaharanaKaratra=LaharanaKaratra).exists():
                #form.add_error("efa misy")
                return redirect("Fitatanana:EfaMisy")
            else:
                form.save()
                #return redirect("Fitatanana:Pejy1")
                #return redirect("Fitatanana:adrana")
                return redirect("Fitatanana:mety")
    else:
        form = Mombamoba2()
    moba = Mpino3.objects.all()
    fikaroana = request.GET.get('q','')
    if not fikaroana:
        fikaroana = date.year
    ita = Mpino3.objects.filter(Anarana__icontains = fikaroana) if fikaroana else None
    Karatra_farany = Mpino3.objects.order_by('-id').values_list('LaharanaKaratra', flat=True).first()
    context = {"form":form,"moba":moba,"fikaroana":fikaroana,"ita":ita,"Karatra_farany":Karatra_farany}

    #return render(request,'Fiagonana/adrana.html',context)
    return render(request, 'Fiagonana/apiditra_mpino.html', context)
def Mety(request):
    return render(request,'Fiagonana/mety.html')
def EfaMisy(request):
    return render(request,'Fiagonana/EfaMisy.html')
#@permission_required('Fitatanana.chage_mpino3')
def Anova(request,anarana):
    Anarana = Mpino3.objects.get(pk= anarana)
    if request.method == 'POST':
        form = Mombamoba2(request.POST,instance=Anarana)
        if form.is_valid():
            form.save()
        return redirect("Tableau:Ijery",anarana=anarana)
    else:
        form = Mombamoba2(instance=Anarana)
        context = {"form":form,"anarana":Anarana}
    return render(request, 'Fiagonana/adrana2.html', context)

#@login_required
def AmpiditraVola(request,id):
    Anarana = Mpino3.objects.get(pk=id)
    if request.method == 'POST':
        form = ApiditraAdidy(request.POST)
        if form.is_valid():
            form.save()
        return redirect("Fitatanana:Pejy1")
    else:
        form = ApiditraAdidy()

    context = {"form": form,"anarana":Anarana}
    return render(request, 'Fiagonana/adrana3.html', context)
#@login_required
def Tahiry(request,id):
    ita = Mpino3.objects.filter(id = id) if id else None
    fikaroana = request.GET.get('q', '')
    ita2 = Adidy.objects.filter(Taona=fikaroana, Mpino=id) if fikaroana else None
    context = {"ita": ita,"ita2":ita2}
    return render(request,'Fiagonana/Tahiry.html',context)

#@login_required
def recherche_payement(request):
    nom = request.GET.get('nom')
    annee = request.GET.get('annee')
    date = request.GET.get('date')
    P = request.GET.get('P')

    if not (nom and annee and date):
        # Si un des critères est manquant, renvoyer un message d'erreur
        return render(request, 'Fiagonana/recherche_payement.html', {
            'message': "Anarana na Karatra, Taona, Daty."
        })

    # Filtrer les cotisations par nom et année
    adidy  = Adidy.objects.filter(
        Mpino__Anarana__icontains=nom,
        Taona=annee
    ) or Adidy.objects.filter(
        Mpino__LaharanaKaratra=nom,
        Taona=annee
    )

    # Chercher le paiement associé à la date
    resultats = []
    resultats_P =[]
    for a in adidy:

        mois_paiements_P = {
            'Janvier': (a.P_J, a.J_Date),
            'Février': (a.P_F, a.F_Date),
            'Mars': (a.P_M, a.Ma_Date),
            'Avril': (a.P_Av, a.Av_Date),
            'Mai': (a.P_Ma, a.Ma_Date),
            'Juin': (a.P_Ji, a.Ji_Date),
            'Juillet': (a.P_Ju, a.Ju_Date),
            'Août': (a.P_Ag, a.Ag_Date),
            'Septembre': (a.P_S, a.S_Date),
            'Octobre': (a.P_Ak, a.Ac_Date),
            'Novembre': (a.P_N, a.N_Date),
            'Décembre': (a.P_D, a.D_Date),
        }

        mois_paiements = {
            'Janvier': (a.J,  a.J_Date),
            'Février': (a.F, a.F_Date),
            'Mars': (a.M, a.Ma_Date),
            'Avril': (a.Av, a.Av_Date),
            'Mai': (a.Ma, a.Ma_Date),
            'Juin': (a.Ji, a.Ji_Date),
            'Juillet': (a.Ju, a.Ju_Date),
            'Août': (a.Ag, a.Ag_Date),
            'Septembre': (a.S, a.S_Date),
            'Octobre': (a.Ak, a.Ac_Date),
            'Novembre': (a.N, a.N_Date),
            'Décembre': (a.D, a.D_Date),
        }

        for mois, (montant, date_paiement) in mois_paiements.items():
            if date_paiement and str(date_paiement) == date:
                resultats.append({
                    'Anarana': a.Mpino.Anarana,
                    'Laharana_Karatra':a.Mpino.LaharanaKaratra,
                    'Taona': a.Taona,
                    'Volana': mois,
                    'Adidy': montant,
                    'Daty': date_paiement,
                })
        for mois, (montant, date_paiement) in mois_paiements_P.items():
            if date_paiement and str(date_paiement) == date:
                resultats_P.append({
                    'Anarana': a.Mpino.Anarana,
                    'Laharana_Karatra': a.Mpino.LaharanaKaratra,
                    'Taona': a.Taona,
                    'Volana': mois,
                    'Adidy': montant,
                    'Daty': date_paiement,
                })

    return render(request, 'Fiagonana/recherche_payement.html', {
        'resultats': resultats,'resultats_P':resultats_P,"Mpino":a.Mpino.M_P,
        'message': "Tsy misy" if not resultats else "",
    })

#@login_required
def AmpiditraAdidyVaovao(request,id):
    Anarana = Mpino3.objects.get(pk=id)
    niditra = request.POST.dict()
    if Mpino3.objects.filter(id=id, M_P="K").exists():
        print("misy")
    print(niditra)
    if request.method == 'POST':
        form = ApiditraAdidy(request.POST)


        if form.is_valid():
            taona = form.cleaned_data['Taona']
            mpino = form.cleaned_data['Mpino']

            P_J = form.cleaned_data['P_J']

            P_F = form.cleaned_data['P_F']

            P_M = form.cleaned_data['P_M']

            P_Av = form.cleaned_data['P_Av']

            P_Ma = form.cleaned_data['P_Ma']

            P_Ji = form.cleaned_data['P_Ji']

            P_Ju = form.cleaned_data['P_Ju']

            P_Ag = form.cleaned_data['P_Ag']

            P_S = form.cleaned_data['P_S']

            P_Ak = form.cleaned_data['P_Ak']

            P_N = form.cleaned_data['P_N']

            P_D = form.cleaned_data['P_D']
            if Adidy.objects.filter(Taona=taona, Mpino=mpino).exists():
                form.add_error("efa misy")
            if Mpino3.objects.filter(Anarana = mpino.id, M_P="K").exists()  and (P_J,P_F,P_Av,P_Ma,P_Ji,P_Ju,P_Ag,P_S,P_Ak,P_N,P_D !=0):
                form.add_error("efa")
            else:
                form.save()
                return redirect("Fitatanana:Pejy1")
    else:


        form = ApiditraAdidy(instance=Adidy)
    diso = niditra
    context = {"form": form,"anarana":Anarana,"diso":diso}
    return render(request, 'Fiagonana/adrana3.html', context)

"""
 Mety
"""
#@permission_required('Fitatanana.chage_adidy')
def AnovaAdidy(request,taona,mpino):
    adidy = Adidy.objects.get(Taona=taona,Mpino=mpino)
    niditra = request.POST.dict()
    print(niditra)
    if request.method == 'POST':
        form =ApiditraAdidyMisy(request.POST, instance=adidy)
        if form.is_valid():
            form.save()
            #return redirect("adrana")
            return HttpResponseRedirect(f"/tahiry/{mpino}")
    else:
        form = ApiditraAdidyMisy(request.POST, instance=adidy)
    diso = niditra
    context = {"form": form, "adidy": adidy, "diso": diso}
    return render(request, 'Fiagonana/adrana6.html', context)

def AmpiditraKatekomen_vaovao(request):
    if request.method == 'POST':
        form = AmpiditraKatekomen(request.POST)
        if form.is_valid():
            Anarana = form.cleaned_data['mpino']
            Taona = form.cleaned_data['Taona']
            Daty_Nidirana = form.cleaned_data['Daty_Nidirana']

            # Créer le compte pour la personne existante
            Katekomen.objects.create(Mpino=Anarana, Taompianarana=Taona, Daty_Nidirana=Daty_Nidirana)

            return redirect("Fitatanana:Pejy1")  # Rediriger vers une page de confirmation
    else:
        form = AmpiditraKatekomen()

    return render(request, 'Fiagonana/Katekomen.html', {'form': form})


def AnovaKatekomen_Misy(request, compte_id):
    katekomen = get_object_or_404(Katekomen, id=compte_id)

    if request.method == 'POST':
        form = AnovaKatekomen(request.POST, instance=katekomen)
        if form.is_valid():
            form.save()
            return redirect('Tableau:Katekomen_L')  # Rediriger après modification
    else:
        form = AnovaKatekomen(instance=katekomen)

    return render(request, 'Fiagonana/AnovaKatekomen.html', {'form': form, 'katekomen': katekomen})
