
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Usuario
from .forms import UsuarioForm

# Class Based Views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class UsuarioListView(ListView):
    model = Usuario
    context_object_name = 'Usuarios'

class UsuarioDetailView(DetailView):
    model = Usuario

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('Usuario_list')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('Usuario_list')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('Usuario_list')