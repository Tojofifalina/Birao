from django.urls import path
from .import views
app_name = "Tableau"
urlpatterns = [
    path('', views.Mpino, name='Tableau'),
    #path('exporte',views.exporte,name='exporte'),
    path('import_Mpino_Exel/', views.import_Mpino_Exel, name='import_Mpino_Exel'),
    path('export_Mpino_Exel/', views.export_Mpino_Exel, name='export__Mpino_Exel'),
    path('import_Adidy_Exel/',views.import_Adidy_Exel,name='import_Adidy_Exel'),
    path('export_Adidy_Exel/',views.export_Adidy_Exell,name='export_Adidy_Exel'),
    #path('Tobana/',views.TobanaMpino,name="Tobana"),
    path('Adidy/',views.Adidy_t,name = 'TobanaAdidy'),

    path('stat/',views.TobanaMpino,name='state'),
    path('Tobana_Arabola/',views.Tobana_Arabola,name='Tobana_Arabola'),
    path('export_Vola_Niditra_Exel/<int:taona>',views.export_Volaniditra,name='Vola_Niditra'),
    path('export_Vola_Nivoka_Exel/<int:taona>',views.export_Volanivoka,name='Vola_Nivoka'),
    path('Katekomen/',views.Katekomen_L,name='Katekomen_L'),
    path('TobanaKatekomen/',views.TobanaKatekomen,name='TobanaKatekomen'),

    path('ijery/<int:anarana>',views.Ijery,name='Ijery'),
    path('ampiditra_fanamarihana/<int:anarana>',views.Ampiditra_Fanamarihana, name='fanamarihana-'),
    path('amafa_Fanamarihana/<int:anarana>',views.Amafa_Fanamarihana,name="amafa_fanamarihana"),
]