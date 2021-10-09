from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse
import bruno_seguros
from bruno_seguros.models import *
# Create your views here.

def index(request):
    return HttpResponse("Teste de conexão")

def clientes(request):
    out = "<h1>Tabela Cliente</h1> <br>"
    for cli in Cliente.objects.all():
        out += "Nome: " + cli.nomes + "<br>"
        out += "Sobrenome: " + cli.sobrenomes + "<br>"
        out += "<a href="" >Editar</a> <a href=""> Deletar</a> <br><br>"
    return HttpResponse(out)

def clientes_datail(request, cliente_id):
    context = {
        'Cliente': Cliente.objects.get(id = cliente_id)
    }
    return render(request, 'bruno_seguros/cliente.html', context)