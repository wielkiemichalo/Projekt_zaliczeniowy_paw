from rest_framework import serializers
from .models import Gatunek, Rezyser, Film, Osoba, Stanowisko 


class GatunekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gatunek
        fields = '__all__'

    def validate_nazwa(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Nazwa gatunku musi zaczynać się wielką literą!")
        return value


class RezyserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezyser
        fields = '__all__'


    def validate(self, data):
        imie = data.get('imie')
        nazwisko = data.get('nazwisko')
        kraj = data.get('kraj')


    
    def validate_imie(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Imię musi zaczynać się wielką literą!")
        if not value.isalpha():
            raise serializers.ValidationError("Imię może zawierać tylko litery!")
        return value

    def validate_nazwisko(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Nazwisko musi zaczynać się wielką literą!")
        if not value.isalpha():
            raise serializers.ValidationError("Nazwisko może zawierać tylko litery!")
        return value

        if kraj and (len(kraj) != 2 or not kraj.isupper()):
            raise serializers.ValidationError({"kraj": "Kod kraju musi mieć 2 wielkie litery (np. PL)."})
        
        return data        


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

    def validate_tytul(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Nazwa filmu musi być wielka literą!")
        return value


class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = "__all__"
        read_only_fields = ['id', 'data_dodania']

    def validate_imie(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Imię musi zaczynać się wielką literą!")
        if not value.isalpha():
            raise serializers.ValidationError("Imię może zawierać tylko litery!")
        return value

    def validate_nazwisko(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Nazwisko musi zaczynać się wielką literą!")
        if not value.isalpha():
            raise serializers.ValidationError("Nazwisko może zawierać tylko litery!")
        return value


class StanowiskoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = "__all__"

    def validate_nazwa(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Nazwa stanowiska musi zaczynać się wielką literą!")
        return value













    