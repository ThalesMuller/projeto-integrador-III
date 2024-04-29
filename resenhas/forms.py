from django import forms
from .models import Resenha

RATINGS =( 
    (1, "★☆☆☆☆"), 
    (2, "★★☆☆☆"), 
    (3, "★★★☆☆"), 
    (4, "★★★★☆"), 
    (5, "★★★★★"), 
) 

class ResenhaForm(forms.ModelForm):

    class Meta:
        model = Resenha    
        
        fields = ['cod_livro', 'texto', 'rating']

        labels = {
            'cod_livro' : 'ISBN',
            'texto' : 'Resenha',
            'rating' : 'Nota',
        }

        widgets = {
            'cod_livro' : forms.NumberInput(),
            'texto' : forms.Textarea(attrs={'placeholder': 'Escreva uma resenha...'}),
            'rating' : forms.RadioSelect(choices=RATINGS)
        }
	