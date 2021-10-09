from django.db import models

# Create your models here.

class Cliente(models.Model):
    nomes = models.CharField(max_length=45)
    sobrenomes = models.CharField(max_length=45)
    rg = models.CharField(max_length=45)
    cpf = models.CharField(max_length=45)
    def __str__(self):
        return f"Cliente(Nome: {self.nomes}, Sobrenome: {self.sobrenomes}, RG: {self.rg}, CPF: {self.cpf})"


class Carro(models.Model):
    marca = models.CharField(max_length=45)
    placa = models.CharField(max_length=45)
    ano = models.CharField(max_length=45)
    apolice_id = models.IntegerField()
    def __str__(self):
        return f"Carro(Marca: {self.marca}, Placa: {self.placa}, Ano: {self.ano}, Apolice_id: {self.apolice_id})"

class Apolice(models.Model):
    nome = models.CharField(max_length=45)
    preco = models.FloatField()
    descricao = models.CharField(max_length=45)
    def __str__(self):
        return f"Apolice(Nome: {self.nome}, Preco: {self.preco}, Descricao: {self.descricao})"


class Accidente(models.Model):
    detalhe = models.CharField(max_length=45)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Acidente(Detalhe: {self.detalhe}, Data: {self.data})"

class Cliente_has_Carro(models.Model):
    cliente_id = models.IntegerField()
    carro_id = models.IntegerField()
    def __str__(self):
        return f"Cliente com Carro(Cliente_id: {self.cliente_id}, Carro_id: {self.carro_id})"

