from django.urls import path
from .import views
app_name = "Fitatanana"
urlpatterns = [
    path('',views.Voloany,name='Pejy1'),
    path('Ikaroka/<str:code>',views.Ikaroka,name='Ikaroka'),
    path('adrana',views.Adrana,name='adrana'),
    path('anova/<int:anarana>',views.Anova,name='anova'),
    path('Apiditravola/<int:id>',views.AmpiditraVola,name='vola'),
    path('tahiry/<int:id>',views.Tahiry,name='tahiry'),
    path('AmpiditraAdidyVaovao/<int:id>', views.AmpiditraAdidyVaovao,name="AmpiditraAdidyVaovao"),
    path('AnovaAdidy/<int:taona>/<int:mpino>',views.AnovaAdidy,name="AnovaAdidy"),
    path('Fikaroana_Adidy/',views.recherche_payement,name='Fikaroana_Adidy'),
    path('AmpiditraKatekonem/',views.AmpiditraKatekomen_vaovao,name='AmpiditraKatekomen'),
    path('HanovaKatekomen/<int:compte_id>',views.AnovaKatekomen_Misy,name = 'AnovaKatekomen_Misy'),
    path('mety/',views.Mety,name='mety'),
path('EfaMisy/',views.EfaMisy,name='EfaMisy'),
]