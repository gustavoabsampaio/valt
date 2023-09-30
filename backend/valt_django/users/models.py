from django.db import models

class Usuario(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, unique=True, null=True, blank=True)
    nascimento = models.DateField()

class Loja(models.Model):
    cpfcnpj = models.CharField(max_length=14, unique=True, null=True, blank=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    logo_url = models.URLField(max_length=255, null=True, blank=True)

class Estilo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

class Peca(models.Model):
    id_loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)
    promocao = models.ForeignKey('Promocao', on_delete=models.SET_NULL, null=True, blank=True)
    colecao = models.CharField(max_length=50, null=True, blank=True)
    ano = models.SmallIntegerField(null=True, blank=True)

class Promocao(models.Model):
    id_loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    id_peca = models.ForeignKey(Peca, on_delete=models.CASCADE, related_name='promocoes')
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    preco_promocao = models.DecimalField(max_digits=12, decimal_places=2)
    porcent_desconto = models.IntegerField()

class Material(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    id_peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    id_loja = models.ForeignKey(Loja, on_delete=models.CASCADE)

class Segue(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    data_seguiu = models.DateField()

class Favorita(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    data_adicao = models.DateField()
    preco_adicao = models.DecimalField(max_digits=12, decimal_places=2)

class Procura(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_estilo = models.ForeignKey(Estilo, on_delete=models.CASCADE)
    data_ini = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

class EstiloPeca(models.Model):
    id_peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    id_estilo = models.ForeignKey(Estilo, on_delete=models.CASCADE)
    caracteristica = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ['id_peca', 'id_estilo']
