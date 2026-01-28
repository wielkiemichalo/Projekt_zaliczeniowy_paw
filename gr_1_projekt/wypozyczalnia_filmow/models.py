from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint

MIESIACE = models.IntegerChoices(
    'Miesiace',
    'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień'
)

FORMAT_FILMU = (
    ('D', 'DVD'),
    ('B', 'Blu-ray'),
    ('V', 'VOD'),
)

class Gatunek(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.TextField(blank=True)
    typowe_motywy = models.CharField(max_length=200, blank=True)
    czy_fabularny = models.BooleanField(default=True)
    ranking_popularnosci = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.nazwa    
        
    class Meta:
        ordering = ['nazwa']
        verbose_name = "Gatunek"
        verbose_name_plural = "Gatunki"
        




class Rezyser(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    kraj = models.CharField(max_length=2, help_text="Kod kraju, np. PL, US, GB")

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    class Meta:
        ordering = ['nazwisko', 'imie']
        verbose_name = "Reżyser"
        verbose_name_plural = "Reżyserzy"
        constraints = [
            UniqueConstraint(fields=['imie', 'nazwisko'], name='unique_rezyser_name')
        ]
           


class Film(models.Model):
    tytul = models.CharField(max_length=168)
    miesiac_premiery = models.IntegerField(choices=MIESIACE.choices, default=MIESIACE.Styczeń)
    format_filmu = models.CharField(max_length=1, choices=FORMAT_FILMU, default='D')
    rezyser = models.ForeignKey(Rezyser, null=True, blank=True, on_delete=models.SET_NULL)
    gatunek = models.ForeignKey(Gatunek, null=True, blank=True, on_delete=models.SET_NULL)
    dostepne_kopie = models.PositiveIntegerField(default=1)
   
    
    def __str__(self):
        return self.tytul    
    
    
    class Meta:
        ordering = ['tytul']
        verbose_name = "Film"
        verbose_name_plural = "Filmy"
        constraints = [
            models.CheckConstraint(condition=models.Q(dostepne_kopie__gte=0), name='kopie_nieujemne'),
        ]
        



PLCIE = models.IntegerChoices(
    'Plcie',
    'Kobieta Mezczyzna Inna'
)
   
class Osoba(models.Model):
    PLEC_WYBOR = (
        ("K", "kobieta"),
        ("M", "mezczyzna"),
        ("I", "inna")
    )
    imie = models.CharField(max_length=50, blank = False, null = False)
    nazwisko = models.CharField(max_length=100, blank = False, null = False)
    plec = models.IntegerField(choices=PLCIE.choices, default=PLCIE.Inna)
    stanowisko = models.ForeignKey('Stanowisko', on_delete=models.CASCADE)
    data_dodania = models.DateField(auto_now_add=True, editable= False)
    wlasciciel = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, default = 1) 
    
    def __str__(self):
        return f"Osoba: {self.imie} {self.nazwisko}"
   
    class Meta:
        ordering = ['nazwisko']
        verbose_name = "Osoba"
        verbose_name_plural = "Osoby"
        permissions = [
            ("can_view_other_persons", "Może przeglądać inne osoby"),
            ("change_osoba_owner", "Może zmienić właściciela rekordu"),
        ]
        

    
class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=50, blank = False, null = False)
    opis = models.TextField(blank = True, null = True) 
    
    def __str__(self):
        return self.nazwa

    class Meta:
        ordering = ['nazwa']
        verbose_name = "Stanowisko"
        verbose_name_plural = "Stanowiska"
        

