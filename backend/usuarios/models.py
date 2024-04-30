from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=64)
    email = models.EmailField(max_length = 254)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField()