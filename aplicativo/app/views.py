import json
from ..models import Fruta
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import FrutaSerializer

class FrutaView(APIView):
    def get(self, request):
        frutas = Fruta.objects.all()
        serializer = FrutaSerializer(frutas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        dicionario = json.loads(request.body)
        print(dicionario)
        fruta = Fruta.pegar_fruta(dicionario['nome'])
        if fruta:
            fruta.save()
            serializer = FrutaSerializer(fruta)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)