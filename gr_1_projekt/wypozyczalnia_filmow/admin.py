from django.contrib import admin

from .models import Gatunek, Rezyser, Film, Osoba, Stanowisko

class GatunekAdmin(admin.ModelAdmin):
    list_display = ["nazwa"]

class RezyserAdmin(admin.ModelAdmin):
    list_display = ["imie", "nazwisko", "kraj"]

class FilmAdmin(admin.ModelAdmin):
    list_display = ["tytul", "gatunek", "rezyser", "ranking_popularności", "dostepne_kopie"]
    list_filter = ["gatunek", "format_filmu", "miesiac_premiery"]
    search_fields = ["tytul"]
    list_editable = ["ranking_popularności", "dostepne_kopie"]

class OsobaAdmin(admin.ModelAdmin):
    list_display = ["imie" , "nazwisko" , "stanowisko", "plec"]
    list_filter = ["stanowisko" , "data_dodania"]
    
class StanowiskoAdmin(admin.ModelAdmin):
    list_filter = ["nazwa"]

admin.site.register(Gatunek, GatunekAdmin)
admin.site.register(Rezyser, RezyserAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)