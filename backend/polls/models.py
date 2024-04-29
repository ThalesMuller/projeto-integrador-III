from django.db import models

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
    rating = models.FloatField()
    created_at = models.DateField()
    created_by = models.IntegerField()

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=64)
    email = models.CharField(max_length=100)
    created_at = models.DateField()
    created_by = models.IntegerField()

class Resenha(models.Model):
    id = models.AutoField(primary_key=True)
    cod_livro = models.IntegerField()
    texto = models.TextField()
    rating = models.FloatField()
    created_at = models.DateField()
    created_by = models.IntegerField()

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    cod_resenha = models.IntegerField()
    texto = models.TextField()
    created_at = models.DateField()
    created_by = models.IntegerField()
