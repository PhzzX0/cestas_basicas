from django.db import models

class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Doador(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class CestaBasica(models.Model):
    descricao = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    data_doacao = models.DateField(auto_now_add=True)
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descricao} - {self.quantidade}"