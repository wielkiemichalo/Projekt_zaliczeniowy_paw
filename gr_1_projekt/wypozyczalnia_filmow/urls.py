from django.urls import path
from . import views

urlpatterns = [
    path('filmy/', views.FilmList.as_view(), name='film-list'),
    path('filmy/<int:pk>/', views.FilmDetail.as_view(), name='film-detail'),
    path('rezyserzy/', views.RezyserList.as_view(), name='rezyser-list'),
    path('osoby/', views.OsobaList.as_view(), name='osoba-list'),
    path('stanowiska/', views.StanowiskoList.as_view(), name='stanowisko-list'),
]