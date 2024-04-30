
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Resenha
from .forms import ResenhaForm

# Class Based Views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class ResenhaListView(ListView):
    model = Resenha
    context_object_name = 'Resenhas'

class ResenhaDetailView(DetailView):
    model = Resenha

class ResenhaCreateView(CreateView):
    model = Resenha
    form_class = ResenhaForm
    success_url = reverse_lazy('Resenha_list')

class ResenhaUpdateView(UpdateView):
    model = Resenha
    form_class = ResenhaForm
    success_url = reverse_lazy('Resenha_list')

class ResenhaDeleteView(DeleteView):
    model = Resenha
    success_url = reverse_lazy('Resenha_list')