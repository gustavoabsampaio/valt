from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views 
from django.urls import re_path 
from . import views
router = DefaultRouter()

router.register(r'usuarios', UsuarioViewSet)





urlpatterns = [
    path('', include(router.urls)),
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token)

]
