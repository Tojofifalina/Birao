"""
       miasa mety
"""
from django.contrib import admin
from .models import Mpino3,Adidy,Katekomen,Fanamarihana
#miasa mety
class AdidyAdmin(admin.ModelAdmin):
    list_display = ('Taona','Mpino','Fitabarany')
    list_filter = ('Mpino','Taona')
    search_fields = ('Taona',)
class Mpino3Admin(admin.ModelAdmin):
    list_display = ('Anarana','Fanampiny','LaharanaKaratra','id')

    search_fields = ('Anarana','LaharanaKaratra')

class KatekomenAdmin(admin.ModelAdmin):
    list_display = ('Mpino',)

class FanamarihanaAdmin(admin.ModelAdmin):
    list_display = ('F_Mpino',)

admin.site.register(Mpino3,Mpino3Admin)
admin.site.register(Adidy,AdidyAdmin)
admin.site.register(Katekomen,KatekomenAdmin)

admin.site.register(Fanamarihana,FanamarihanaAdmin)
