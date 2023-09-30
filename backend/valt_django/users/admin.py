from django.contrib import admin
from .models import Usuario, Loja, Estilo, Peca, Promocao, Material, Segue, Favorita, Procura, EstiloPeca

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'email', 'nome', 'sobrenome', 'nickname', 'nascimento')

class LojaAdmin(admin.ModelAdmin):
    list_display = ('cpfcnpj', 'nome', 'email', 'telefone', 'logo_url')

class EstiloAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

class PecaAdmin(admin.ModelAdmin):
    list_display = ('id_loja', 'nome', 'preco', 'descricao', 'disponivel', 'promocao', 'colecao', 'ano')

class PromocaoAdmin(admin.ModelAdmin):
    list_display = ('id_loja', 'id_peca', 'data_inicio', 'data_fim', 'preco_promocao', 'porcent_desconto')

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id_peca', 'id_loja')

class SegueAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'id_loja', 'data_seguiu')

class FavoritaAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'id_peca', 'data_adicao', 'preco_adicao')

class ProcuraAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'id_estilo', 'data_ini', 'data_fim')

class EstiloPecaAdmin(admin.ModelAdmin):
    list_display = ('id_peca', 'id_estilo', 'caracteristica')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Loja, LojaAdmin)
admin.site.register(Estilo, EstiloAdmin)
admin.site.register(Peca, PecaAdmin)
admin.site.register(Promocao, PromocaoAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Segue, SegueAdmin)
admin.site.register(Favorita, FavoritaAdmin)
admin.site.register(Procura, ProcuraAdmin)
admin.site.register(EstiloPeca, EstiloPecaAdmin)
