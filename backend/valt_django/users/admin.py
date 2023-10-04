from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'email', 'nome', 'sobrenome', 'nickname', 'nascimento')


admin.site.register(Usuario, UsuarioAdmin)
