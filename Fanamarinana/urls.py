from django.urls import path
from .import views
app_name = 'Fanamarinana'
urlpatterns = [
    path('login/',views.anokatra,name= 'anokatra'),
    path('logout/',views.anidy,name= 'anidy')
]