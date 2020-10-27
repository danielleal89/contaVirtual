from django.forms import ModelForm
from .models import *

#Classe com os dados do formulário para cadastrar conta
class ContaForm(ModelForm):
    class Meta:
        model = Conta
        fields = ['nome', 'cpf']

#Classe com os dados do formulário para sacar ou depositar valor
class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['valor']
