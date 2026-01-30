from django import forms
from .models import Gatunek, Rezyser, Film, Osoba, Stanowisko 

class OsobaForm(forms.ModelForm):
    class Meta:
        model = Osoba
        fields = ['imie', 'nazwisko', 'plec', 'stanowisko']



class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['tytul', 'miesiac_premiery','format_filmu','rezyser','gatunek', 'dostepne_kopie' ]
            
           


class StanowiskoForm(forms.ModelForm):
    class Meta:
        model = Stanowisko
        fields = ['nazwa', 'opis']
            

       
