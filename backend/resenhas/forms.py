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
        
        fields = "__all__"

        labels = {
            'cod_livro' : 'Livro',
            'texto' : 'Resenha',
            'rating' : 'Nota',
        }

        widgets = {
            'texto' : forms.Textarea(attrs={'placeholder': 'Escreva uma resenha...'}),
            'rating' : forms.RadioSelect(choices=RATINGS)
        }
	