from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("livros/", include("livros.urls")),
    path("usuarios/", include("usuarios.urls")),
    path("resenhas/", include("resenhas.urls")),
    path("comentarios/", include("comentarios.urls")),
]