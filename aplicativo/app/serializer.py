from ..models import Fruta, Nutricao
from rest_framework import serializers
import requests
class NutricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutricao
        fields = '__all__'
        
class FrutaSerializer(serializers.ModelSerializer):
    nutritions = NutricaoSerializer(many=False, read_only=True)
    class Meta:
        model = Fruta
        fields = ['name', 'family', 'genus', 'nutritions']


    def create(self, validated_data):
        nutricao_data = validated_data.pop('nutritions')
        nutricao = Nutricao.objects.create(**nutricao_data)
        fruta = Fruta.objects.create(nutritions=nutricao, **validated_data)

        return fruta
    
    @staticmethod
    def pegar_fruta(nome_fruta):
        url = f'https://www.fruityvice.com/api/fruit/{nome_fruta}'
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return FrutaSerializer(data=resposta.json())
        else:
            resposta.raise_for_status()
