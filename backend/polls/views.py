from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_livros(request):
    obj = Livro.objects.all()
    template_name = 'null'
    context = {'obj': obj}
    return render(request, template_name, context)