from rest_framework import viewsets
from rest_framework.response import  Response
from rest_framework.decorators import action
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    @action(detail=True, methods=['get'])
    def get_usuario_by_id(sef, request, pk=None):
        usuario = self.get_object()
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
