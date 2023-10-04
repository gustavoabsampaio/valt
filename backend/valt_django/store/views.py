from django.shortcuts import render
from rest_framework import viewsets
from .models import Loja, Estilo, Peca, Promocao, Material, Favorita, Procura, EstiloPeca, Segue
from .serializers import (
    LojaSerializer, EstiloSerializer, PecaSerializer, PromocaoSerializer, 
    MaterialSerializer, FavoritaSerializer, ProcuraSerializer, EstiloPecaSerializer, SegueSerializer
)

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer

class EstiloViewSet(viewsets.ModelViewSet):
    queryset = Estilo.objects.all()
    serializer_class = EstiloSerializer

class PecaViewSet(viewsets.ModelViewSet):
    queryset = Peca.objects.all()
    serializer_class = PecaSerializer

class PromocaoViewSet(viewsets.ModelViewSet):
    queryset = Promocao.objects.all()
    serializer_class = PromocaoSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class FavoritaViewSet(viewsets.ModelViewSet):
    queryset = Favorita.objects.all()
    serializer_class = FavoritaSerializer

class ProcuraViewSet(viewsets.ModelViewSet):
    queryset = Procura.objects.all()
    serializer_class = ProcuraSerializer

class EstiloPecaViewSet(viewsets.ModelViewSet):
    queryset = EstiloPeca.objects.all()
    serializer_class = EstiloPecaSerializer

class SegueViewSet(viewsets.ModelViewSet):
    queryset = Segue.objects.all()
    serializer_class = SegueSerializer
