# Generated by Django 4.2.5 on 2023-10-04 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_estilopeca_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpfcnpj', models.CharField(blank=True, max_length=14, null=True, unique=True)),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('logo_url', models.URLField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=12)),
                ('descricao', models.TextField()),
                ('disponivel', models.BooleanField(default=True)),
                ('colecao', models.CharField(blank=True, max_length=50, null=True)),
                ('ano', models.SmallIntegerField(blank=True, null=True)),
                ('id_loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.loja')),
            ],
        ),
        migrations.CreateModel(
            name='Segue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_seguiu', models.DateField()),
                ('id_loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.loja')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Promocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('preco_promocao', models.DecimalField(decimal_places=2, max_digits=12)),
                ('porcent_desconto', models.IntegerField()),
                ('id_loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.loja')),
                ('id_peca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promocoes', to='store.peca')),
            ],
        ),
        migrations.CreateModel(
            name='Procura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_ini', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('id_estilo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.estilo')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='peca',
            name='promocao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.promocao'),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True)),
                ('id_loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.loja')),
                ('id_peca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.peca')),
            ],
        ),
        migrations.CreateModel(
            name='Favorita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_adicao', models.DateField()),
                ('preco_adicao', models.DecimalField(decimal_places=2, max_digits=12)),
                ('id_peca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.peca')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='EstiloPeca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caracteristica', models.TextField(blank=True, null=True)),
                ('id_estilo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.estilo')),
                ('id_peca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.peca')),
            ],
            options={
                'unique_together': {('id_peca', 'id_estilo')},
            },
        ),
    ]
