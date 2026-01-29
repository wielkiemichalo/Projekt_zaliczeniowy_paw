from rest_framework import generics
from .models import Film, Rezyser, Gatunek, Osoba, Stanowisko
from .serializers import (
    FilmSerializer, RezyserSerializer, GatunekSerializer, 
    OsobaSerializer, StanowiskoSerializer
)

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
