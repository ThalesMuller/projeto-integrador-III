from django.db import models
from resenhas.models import Resenha
from usuarios.models import Usuario

# Create your models here.
class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    cod_resenha = models.ForeignKey(Resenha, models.CASCADE)
    texto = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(Usuario, models.CASCADE)