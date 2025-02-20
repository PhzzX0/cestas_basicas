from django import forms
from .models import Instituicao, Doador, CestaBasica

class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = ['nome', 'endereco', 'telefone', 'email']

class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = ['nome', 'endereco', 'telefone', 'email']

class CestaBasicaForm(forms.ModelForm):
    class Meta:
        model = CestaBasica
        fields = ['descricao', 'quantidade', 'doador', 'instituicao']