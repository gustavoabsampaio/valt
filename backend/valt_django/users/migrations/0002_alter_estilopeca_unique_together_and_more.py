# Generated by Django 4.2.5 on 2023-10-04 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='estilopeca',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='estilopeca',
            name='id_estilo',
        ),
        migrations.RemoveField(
            model_name='estilopeca',
            name='id_peca',
        ),
        migrations.RemoveField(
            model_name='favorita',
            name='id_peca',
        ),
        migrations.RemoveField(
            model_name='favorita',
            name='id_usuario',
        ),
        migrations.RemoveField(
            model_name='material',
            name='id_loja',
        ),
        migrations.RemoveField(
            model_name='material',
            name='id_peca',
        ),
        migrations.RemoveField(
            model_name='peca',
            name='id_loja',
        ),
        migrations.RemoveField(
            model_name='peca',
            name='promocao',
        ),
        migrations.RemoveField(
            model_name='procura',
            name='id_estilo',
        ),
        migrations.RemoveField(
            model_name='procura',
            name='id_usuario',
        ),
        migrations.RemoveField(
            model_name='promocao',
            name='id_loja',
        ),
        migrations.RemoveField(
            model_name='promocao',
            name='id_peca',
        ),
        migrations.RemoveField(
            model_name='segue',
            name='id_loja',
        ),
        migrations.RemoveField(
            model_name='segue',
            name='id_usuario',
        ),
        migrations.DeleteModel(
            name='Estilo',
        ),
        migrations.DeleteModel(
            name='EstiloPeca',
        ),
        migrations.DeleteModel(
            name='Favorita',
        ),
        migrations.DeleteModel(
            name='Loja',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='Peca',
        ),
        migrations.DeleteModel(
            name='Procura',
        ),
        migrations.DeleteModel(
            name='Promocao',
        ),
        migrations.DeleteModel(
            name='Segue',
        ),
    ]
