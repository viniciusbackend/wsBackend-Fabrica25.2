import json
from ..models import Fruta, Nutricao
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import FrutaSerializer, NutricaoSerializer

class FrutaView(APIView):
    def get(self, request):
        frutas = Fruta.objects.all()
        serializer = FrutaSerializer(frutas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        dicionario = json.loads(request.body)
        print(dicionario)
        fruta = FrutaSerializer.pegar_fruta(dicionario['nome'])
        
        if fruta.is_valid():
            fruta.save()
            return Response(fruta.data, status=status.HTTP_201_CREATED)
        else:
            print(fruta.error_messages)
            print(fruta.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)