from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario    
        
        fields = '__all__'

        labels = {
            'cod_resenha' : 'Resenha',
            'texto' : 'Comentário'
        }

        widgets = {
            'cod_livro' : forms.NumberInput(),
            'texto' : forms.Textarea(attrs={'placeholder': 'Escreva um comentário...'})
        }
	