from django.urls import path
from .import views
app_name = "Vola"
urlpatterns = [
    path('Apiditra_vola/',views.Vola_Niditra,name='Vola_Niditra'),
    path('FamoahaMbola/',views.Vola_Nivoka,name='Vola_Nivoka'),

]