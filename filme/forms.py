from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class FormHomepage(forms.Form):
    email = forms.EmailField(label=False) # pra tirar label do campo email da homepage


class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    # OBS: class meta é o padrão do django -informar qual o modelo padrão que vai criar o formulario
    class Meta:
        model = Usuario
        # campos padroes do django, só acrescenti campo email
        # campos da page criar usuario
        fields = ('username', 'email', 'password1', 'password2')