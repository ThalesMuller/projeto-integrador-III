# Generated by Django 5.0.4 on 2024-04-29 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('resenhas', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='cod_resenha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resenhas.resenha'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario'),
        ),
    ]