from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro    
        fields = "__all__"

        labels = {
            'isbn': 'ISBN',
            'titulo': 'Titulo',
            'genero': 'Gênero',
            'autor': 'Autor',
            'editora': 'Editora',
            'ano_publicacao': 'Ano da Publicação',
            'numero_paginas': 'Número de Páginas'
        }

        widgets = {
            'isbn': forms.TextInput(attrs={'placeholder': 'ex. 978 – 85 – 333 – 0227 – 3'}),
            'titulo': forms.TextInput(attrs={'placeholder': 'Nome do Livro'}),
            'genero': forms.TextInput(attrs={'placeholder': 'Gênero Textual'}),
            'autor': forms.TextInput(attrs={'placeholder': 'Nome do Autor'}),
            'editora': forms.TextInput(attrs={'placeholder': 'Nome da Editora'}),
            'ano_publicacao': forms.NumberInput(attrs={'placeholder': 'ex. 2024'}),
            'numero_paginas': forms.NumberInput(attrs={'placeholder': 'ex. 250'})
        }
	