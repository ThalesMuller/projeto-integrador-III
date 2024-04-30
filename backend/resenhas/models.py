from django.db import models
from livros.models import Livro
from usuarios.models import Usuario

# Create your models here.
class Resenha(models.Model):
    id = models.AutoField(primary_key=True)
    cod_livro = models.ForeignKey(Livro, models.CASCADE)
    texto = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(Usuario, models.DO_NOTHING)