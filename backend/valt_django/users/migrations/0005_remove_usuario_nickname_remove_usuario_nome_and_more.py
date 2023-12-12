# Generated by Django 4.2.5 on 2023-12-11 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='senha',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='sobrenome',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
