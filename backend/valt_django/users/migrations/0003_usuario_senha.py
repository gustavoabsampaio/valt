# Generated by Django 4.2.5 on 2023-12-11 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_estilopeca_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='senha',
            field=models.CharField(default='value', max_length=20),
            preserve_default=False,
        ),
    ]