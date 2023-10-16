from django.shortcuts import render
from datetime import date
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import  Response
from .models import Loja, Estilo, Peca, Promocao, Material, Favorita, Procura, EstiloPeca, Segue
from .serializers import (
    LojaSerializer, EstiloSerializer, PecaSerializer, PromocaoSerializer, 
    MaterialSerializer, FavoritaSerializer, ProcuraSerializer, EstiloPecaSerializer, SegueSerializer
)

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer
    
    @action(detail=True, methods=['GET'])
    def get_loja_by_id(sef, request, pk=None):
        loja = self.get_object()
        serializer = LojaSerializer(loja)
        return Response(serializer.data)

class EstiloViewSet(viewsets.ModelViewSet):
    queryset = Estilo.objects.all()
    serializer_class = EstiloSerializer

class PecaViewSet(viewsets.ModelViewSet):
    queryset = Peca.objects.all()
    serializer_class = PecaSerializer
    
    @action(detail=True, methods=['GET'])
    def get_peca_by_id(sef, request, pk=None):
        peca = self.get_object()
        serializer = PecaSerializer(peca)
        return Response(serializer.data)


class PromocaoViewSet(viewsets.ModelViewSet):
    queryset = Promocao.objects.all()
    serializer_class = PromocaoSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class FavoritaViewSet(viewsets.ModelViewSet):
    queryset = Favorita.objects.all()
    serializer_class = FavoritaSerializer
    
    @action(detail=True, methods=['POST'])
    def add_to_favorites(self, request, id_peca, pk=None):
        try:
            peca = Peca.objects.get(pk=id_peca)
            favorita, created = Favorita.objects.get_or_create(
                id_usuario = request.usuario,
                peca = peca,
                data_adicao = date.today(),
                preco_adicao = request.data.get('preco_adicao')
                )
            
            if created:
                return Response({'message': 'Produto adicionado aos favoritos.'}, status=201)
        except Peca.DoesNotExist:
            return Response({'message': 'Peça não encontrada.'}, status=404)

class ProcuraViewSet(viewsets.ModelViewSet):
    queryset = Procura.objects.all()
    serializer_class = ProcuraSerializer

class EstiloPecaViewSet(viewsets.ModelViewSet):
    queryset = EstiloPeca.objects.all()
    serializer_class = EstiloPecaSerializer

class SegueViewSet(viewsets.ModelViewSet):
    queryset = Segue.objects.all()
    serializer_class = SegueSerializer
