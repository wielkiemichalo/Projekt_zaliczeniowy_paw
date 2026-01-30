from rest_framework import generics
from .models import Film, Rezyser, Gatunek, Osoba, Stanowisko
from .serializers import (
    FilmSerializer, RezyserSerializer, GatunekSerializer, 
    OsobaSerializer, StanowiskoSerializer
)
import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework import generics, status
from rest_framework.response import Response
from .forms import OsobaForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import random
from .forms import FilmForm
from django.contrib.auth.decorators import user_passes_test
from .forms import StanowiskoForm





class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer



class RezyserList(generics.ListCreateAPIView):
    queryset = Rezyser.objects.all()
    serializer_class = RezyserSerializer

class RezyserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rezyser.objects.all()
    serializer_class = RezyserSerializer



class GatunekList(generics.ListCreateAPIView):
    queryset = Gatunek.objects.all()
    serializer_class = GatunekSerializer

class GatunekDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gatunek.objects.all()
    serializer_class = GatunekSerializer



class OsobaList(generics.ListCreateAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer

class OsobaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer



class StanowiskoList(generics.ListCreateAPIView):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer

class StanowiskoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer

def welcome(request):
    now = datetime.datetime.now()
    return render(request, 'welcome.html', {'current_time': now})


def film_list_html(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('film-list-html')
    else:
        form = FilmForm()

    filmy = Film.objects.all()
    
    return render(request, "wypozyczalnia_filmow/film/list.html", {
        'filmy': filmy, 
        'form': form
    })

def film_detail_html(request, id):
    film = get_object_or_404(Film, id=id)
    if request.method == "POST":
        film.delete()
        return redirect('film-list-html')
    return render(request, "wypozyczalnia_filmow/film/detail.html", {'film': film})


def film_create_html(request):
    if request.method == "POST":
        serializer = FilmSerializer(data=request.POST)
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('film-list-html')
    else:
        form = FilmForm()
    
    return render(request, "wypozyczalnia_filmow/film/create.html", {'form': form})

def film_edit(request, id):
    film = get_object_or_404(Film, id=id)
    if request.method == "POST":
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect('film-list-html')
    else:
        form = FilmForm(instance=film)
    return render(request, 'wypozyczalnia_filmow/film/form.html', {'form': form, 'title': 'Edytuj film'})


def film_search(request):
    query = request.GET.get('q') 
    if query:
        filmy = Film.objects.filter(tytul__icontains=query)
    else:
        filmy = Film.objects.all()
    

    return render(request, 'wypozyczalnia_filmow/film/search.html', {'filmy': filmy, 'query': query})


def random_movie_page(request):
    wszystkie_filmy = Film.objects.all()
    
    losowy_film = None
    if wszystkie_filmy.exists():
        losowy_film = random.choice(wszystkie_filmy)
    

    return render(request, 'wypozyczalnia_filmow/film/random_result.html', {
        'film': losowy_film
    })



def osoba_list_html(request):
    osoby = Osoba.objects.all()
    return render(request, "wypozyczalnia_filmow/osoba/list.html", {'osoby': osoby})    



def osoba_detail_html(request, id):
    osoba = get_object_or_404(Osoba, id=id)
    if request.method == "POST":
        osoba.delete()
        return redirect('osoba-list-html')
    return render(request, "wypozyczalnia_filmow/osoba/detail.html", {'osoba': osoba})


@user_passes_test(lambda u: u.is_superuser)
def osoba_create_html(request):
    stanowiska = Stanowisko.objects.all()
    if request.method == "POST":
        imie = request.POST.get('imie')
        nazwisko = request.POST.get('nazwisko')
        
        
        plec_raw = request.POST.get('plec')

        plec = 2 if plec_raw in ['K', '2'] else 1 
        
        stanowisko_id = request.POST.get('stanowisko')

        serializer = OsobaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('osoba-list-html')
        errors = serializer.errors

        if imie and nazwisko and stanowisko_id:
            stanowisko_obj = get_object_or_404(Stanowisko, id=stanowisko_id)
            Osoba.objects.create(
                imie=imie, 
                nazwisko=nazwisko, 
                plec=plec, 
                stanowisko=stanowisko_obj
            )
            return redirect('osoba-list-html')
            
    return render(request, "wypozyczalnia_filmow/osoba/create.html", {'stanowiska': stanowiska})

@user_passes_test(lambda u: u.is_superuser)
def osoba_edit_html(request, id):
    osoba = get_object_or_404(Osoba, id=id)
    errors = None
    if request.method == "POST":
        data = request.POST.copy()
        data['plec'] = 2 if data.get('plec') in ['K', '2', 'Kobieta'] else 1
        serializer = OsobaSerializer(instance=osoba, data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('osoba-list-html')
        errors = serializer.errors
    return render(request, "wypozyczalnia_filmow/osoba/create.html", {
        'osoba': osoba, 
        'errors': errors, 
        'stanowiska': Stanowisko.objects.all()
    })

@user_passes_test(lambda u: u.is_superuser)
def osoba_list_html(request):
    osoby = Osoba.objects.all()
    return render(request, 'wypozyczalnia_filmow/osoba/list.html', {'osoby': osoby})


def gatunek_list_html(request):
    gatunki = Gatunek.objects.all()
    return render(request, "wypozyczalnia_filmow/gatunek/list.html", {'gatunki': gatunki})

def gatunek_create_html(request):
    if request.method == "POST":
        serializer = GatunekSerializer(data=request.POST)
        nazwa = request.POST.get('nazwa')
        opis = request.POST.get('opis')
        typowe_motywy = request.POST.get('typowe_motywy')
        czy_fabularny = request.POST.get('czy_fabularny') == 'on'

        if nazwa:
            Gatunek.objects.create(
                nazwa=nazwa, opis=opis, 
                typowe_motywy=typowe_motywy, czy_fabularny=czy_fabularny
            )
            return redirect('gatunek-list-html')
    return render(request, "wypozyczalnia_filmow/gatunek/create.html")

def gatunek_detail_html(request, id):
    gatunek = get_object_or_404(Gatunek, id=id)
    
    if request.method == "POST":
        gatunek.delete()
        return redirect('gatunek-list-html')
        
    return render(request, "wypozyczalnia_filmow/gatunek/detail.html", {'gatunek': gatunek})

def gatunek_edit_html(request, id):
    gatunek = get_object_or_404(Gatunek, id=id)
    errors = None
    if request.method == "POST":
        serializer = GatunekSerializer(instance=gatunek, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('gatunek-list-html')
        errors = serializer.errors
    return render(request, "wypozyczalnia_filmow/gatunek/create.html", {
        'gatunek': gatunek, 
        'errors': errors
    })


def rezyser_list_html(request):
    rezyserzy = Rezyser.objects.all()
    return render(request, "wypozyczalnia_filmow/rezyser/list.html", {'rezyserzy': rezyserzy})

def rezyser_create_html(request):
    if request.method == "POST":
        serializer = RezyserSerializer(data=request.POST)
        imie = request.POST.get('imie')
        nazwisko = request.POST.get('nazwisko')
        kraj = request.POST.get('kraj')
        if imie and nazwisko:
            Rezyser.objects.create(imie=imie, nazwisko=nazwisko, kraj=kraj)
            return redirect('rezyser-list-html')
    return render(request, "wypozyczalnia_filmow/rezyser/create.html")

def rezyser_detail_html(request, id):
    rezyser = get_object_or_404(Rezyser, id=id)
    if request.method == "POST":
        rezyser.delete()
        return redirect('rezyser-list-html')
    return render(request, "wypozyczalnia_filmow/rezyser/detail.html", {'rezyser': rezyser})


def rezyser_edit_html(request, id):
    rezyser = get_object_or_404(Rezyser, id=id)
    errors = None
    if request.method == "POST":
        serializer = RezyserSerializer(instance=rezyser, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('rezyser-list-html')
        errors = serializer.errors
    return render(request, "wypozyczalnia_filmow/rezyser/create.html", {
        'rezyser': rezyser, 
        'errors': errors
    })




def film_detail_html(request, id):
    film = get_object_or_404(Film, id=id)
    if request.method == "POST":
        film.delete()
        return redirect('film-list-html')
    return render(request, "wypozyczalnia_filmow/film/detail.html", {'film': film})

@user_passes_test(lambda u: u.is_superuser)
def stanowisko_list_html(request):
    stanowiska = Stanowisko.objects.all()
    return render(request, 'wypozyczalnia_filmow/stanowisko/list.html', {'stanowiska': stanowiska})

@user_passes_test(lambda u: u.is_superuser)
def stanowisko_create_html(request):
    if request.method == "POST":
        form = StanowiskoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stanowisko-list-html')
    else:
        form = StanowiskoForm()
    return render(request, 'wypozyczalnia_filmow/stanowisko/create.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def stanowisko_detail_html(request, id):
    stanowisko = get_object_or_404(Stanowisko, id=id)
    return render(request, 'wypozyczalnia_filmow/stanowisko/detail.html', {'stanowisko': stanowisko})

@user_passes_test(lambda u: u.is_superuser)
def stanowisko_delete_html(request, id):
    stanowisko = get_object_or_404(Stanowisko, id=id)
    if request.method == "POST":
        stanowisko.delete()
        return redirect('stanowisko-list-html')
    return redirect('stanowisko-detail-html', id=id)


@user_passes_test(lambda u: u.is_superuser)
def stanowisko_edit_html(request, id):
    stanowisko = get_object_or_404(Stanowisko, id=id)
    errors = None
    if request.method == "POST":
        serializer = StanowiskoSerializer(instance=stanowisko, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('stanowisko-list-html')
        errors = serializer.errors
    return render(request, 'wypozyczalnia_filmow/stanowisko/create.html', {
        'stanowisko': stanowisko, 
        'errors': errors
    })




def rejestracja(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('osoba-list-html') 
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})