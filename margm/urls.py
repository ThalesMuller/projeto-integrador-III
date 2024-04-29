from django.contrib import admin
from . import views
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name="Home"),
    path("livros/", include("livros.urls")),
    path("usuarios/", include("usuarios.urls")),
    path("resenhas/", include("resenhas.urls")),
    path("comentarios/", include("comentarios.urls")),    
    path("contas/", include("django.contrib.auth.urls")),
]