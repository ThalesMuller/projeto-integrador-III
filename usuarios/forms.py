from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):

    class Meta:
        password = forms.CharField(widget=forms.PasswordInput())
        model = Usuario    
        
        fields = '__all__'

        labels = {
            'login' : 'Login',
            'email' : 'Email',
            'senha' : 'Senha'
        }

        widgets = {
            'login' : forms.TextInput(attrs={'placeholder': 'ex. 978 – 85 – 333 – 0227 – 3'}),
            'email' : forms.EmailInput(),
            'senha' : forms.PasswordInput()
        }
	