from django.db import models

# Create your models here.
class Resenha(models.Model):
    id = models.AutoField(primary_key=True)
    cod_livro = models.IntegerField()
    texto = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    created_by = models.IntegerField()