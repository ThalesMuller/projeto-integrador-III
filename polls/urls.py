from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('livros/', views.get_livros, name='get_livros'),
    ]
