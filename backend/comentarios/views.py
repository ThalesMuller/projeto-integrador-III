
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Comentario
from .forms import ComentarioForm

# Class Based Views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class ComentarioListView(ListView):
    model = Comentario
    context_object_name = 'Comentarios'

class ComentarioDetailView(DetailView):
    model = Comentario

class ComentarioCreateView(CreateView):
    model = Comentario
    form_class = ComentarioForm
    success_url = reverse_lazy('Comentario_list')

class ComentarioUpdateView(UpdateView):
    model = Comentario
    form_class = ComentarioForm
    success_url = reverse_lazy('Comentario_list')

class ComentarioDeleteView(DeleteView):
    model = Comentario
    success_url = reverse_lazy('Comentario_list')