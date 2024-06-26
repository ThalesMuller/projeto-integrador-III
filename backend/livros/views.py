from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from .models import Livro
from .forms import LivroForm

# Class Based Views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class LivroListView(ListView):
    model = Livro
    context_object_name = 'Livros'

    def get_queryset(self):
        return Livro.objects.filter(Q(titulo=self.request.query) | Q(autor=self.request.query) | Q(usuario=self.request.query))

class LivroDetailView(DetailView):
    model = Livro

class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    success_url = reverse_lazy('Livro_list')

class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    success_url = reverse_lazy('Livro_list')

class LivroDeleteView(DeleteView):
    model = Livro
    success_url = reverse_lazy('Livro_list')