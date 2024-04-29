from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13)
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    numero_paginas = models.IntegerField()
    rating = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Usuario, models.DO_NOTHING)