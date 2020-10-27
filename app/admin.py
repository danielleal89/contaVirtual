from django.contrib import admin
from .models import *

#Insere no painel admin
admin.site.register(Conta)
admin.site.register(Transacao)