import requests
from django.db import models

class Fruta(models.Model):
    nome = models.CharField(max_length=155)
    familia = models.CharField(max_length=155)
    genero = models.CharField(max_length=155)

    def __str__(self):
        return self.nome
    
    @staticmethod
    def pegar_fruta(nome_fruta):
        url = f'https://www.fruityvice.com/api/fruit/{nome_fruta}'
        resposta = requests.get(url)
        if resposta.status_code == 200:
            fruta_json = resposta.json()
            return Fruta(
                nome = fruta_json['name'],
                familia = fruta_json['family'],
                genero = fruta_json['genus'],
            )