from django.contrib import admin

from .models import Gatunek, Rezyser, Film, Osoba, Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    list_display = ["imie" , "nazwisko" , "stanowisko"]
    list_filter = ["stanowisko" , "data_dodania"]
    
class StanowiskoAdmin(admin.ModelAdmin):
    list_filter = ["nazwa"]

admin.site.register(Gatunek)
admin.site.register(Rezyser)
admin.site.register(Film)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)