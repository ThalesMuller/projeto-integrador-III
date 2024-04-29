from django.db import models

# Create your models here.
class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    cod_resenha = models.IntegerField()
    texto = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    created_by = models.IntegerField()