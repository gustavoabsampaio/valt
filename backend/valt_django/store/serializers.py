# serializers.py
from rest_framework import serializers
from .models import (
    Loja,
    Estilo,
    Peca,
    Promocao,
    Material,
    Segue,
    Favorita,
    Procura,
    EstiloPeca,
)


class EstiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estilo
        fields = '__all__'
    

class PromocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocao
        fields = '__all__'


class PecaSerializer(serializers.ModelSerializer):
    promocoes = PromocaoSerializer(many=True, read_only=True, source='promocoes')
    
    class Meta:
        model = Peca
        fields = [f.name for f in Peca._meta.fields] + ['promocoes']

class LojaSerializer(serializers.ModelSerializer):
    pecas = PecaSerializer(many=True, read_only=True, source='peca_set')
    
    class Meta:
        model = Loja
        fields = [f.name for f in Loja._meta.fields] + ['pecas']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class SegueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segue
        fields = '__all__'


class FavoritaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorita
        fields = '__all__'


class ProcuraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procura
        fields = '__all__'


class EstiloPecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstiloPeca
        fields = '__all__'

