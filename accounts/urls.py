from django.urls import path
from .import views
app_name = "accounts"
urlpatterns = [
    path('login/',views.anokatra,name= 'login'),
    path('anidy',views.anidy,name= 'anidy')
]