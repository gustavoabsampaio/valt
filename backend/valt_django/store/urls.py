from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (LojaViewSet, EstiloViewSet, PecaViewSet, PromocaoViewSet, MaterialViewSet, FavoritaViewSet, ProcuraViewSet, EstiloPecaViewSet, SegueViewSet)


router = DefaultRouter()

router.register(r'lojas', LojaViewSet)

router.register(r'estilos', EstiloViewSet)

router.register(r'pecas', PecaViewSet)

router.register(r'promocoes', PromocaoViewSet)

router.register(r'materiais', MaterialViewSet)

router.register(r'favoritas', FavoritaViewSet)

router.register(r'procuras', ProcuraViewSet)

router.register(r'estilospecas', EstiloPecaViewSet)

router.register(r'segues', SegueViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls