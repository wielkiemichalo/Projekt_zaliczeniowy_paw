from django.urls import path, include
from . import views

urlpatterns = [
    
    path('filmy/', views.FilmList.as_view(), name='film-list'),
    path('filmy/<int:pk>/', views.FilmDetail.as_view(), name='film-detail'),
    path('rezyserzy/', views.RezyserList.as_view(), name='rezyser-list'),
    path('osoby/', views.OsobaList.as_view(), name='osoba-list'),
    path('stanowiska/', views.StanowiskoList.as_view(), name='stanowisko-list'),
    path('welcome/', views.welcome, name='welcome'),

    
    path('html/osoby/', views.osoba_list_html, name='osoba-list-html'),
    path('html/osoby/<int:id>/', views.osoba_detail_html, name='osoba-detail-html'),
    path('html/osoby/dodaj/', views.osoba_create_html, name='osoba-create'),
    path('html/osoby/dodaj_django/', views.osoba_create_django_form, name='osoba-create-django'),
  
    
    
    path('html/filmy/', views.film_list_html, name='film-list-html'),
    path('html/filmy/<int:id>/', views.film_detail_html, name='film-detail-html'),
    path('html/filmy/dodaj/', views.film_create, name='film-create-html'),
    path('html/filmy/edytuj/<int:id>/', views.film_edit, name='film-edit-html'),
    path('html/filmy/szukaj/', views.film_search, name='film-search-html'),
    path('html/filmy/losuj/', views.random_movie_page, name='film-random-page'),

    path('html/gatunki/', views.gatunek_list_html, name='gatunek-list-html'),
    path('html/gatunki/dodaj/', views.gatunek_create_html, name='gatunek-create-html'),
    path('html/gatunki/<int:id>/', views.gatunek_detail_html, name='gatunek-detail-html'),
    

    path('html/rezyserzy/', views.rezyser_list_html, name='rezyser-list-html'), 
    path('html/rezyserzy/<int:id>/', views.rezyser_detail_html, name='rezyser-detail-html'), 
    path('html/rezyserzy/nowy/', views.rezyser_create_html, name='rezyser-create-html'),


    path('accounts/', include('django.contrib.auth.urls')),
    path('rejestracja/', views.rejestracja, name='register'),

]

