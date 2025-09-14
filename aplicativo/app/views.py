import json
from ..models import Fruta, Nutricao
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import FrutaSerializer, NutricaoSerializer
from rest_framework.permissions import IsAuthenticated


class FrutasView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        frutas = Fruta.objects.all()
        serializer = FrutaSerializer(frutas, many=True)
        return Response(serializer.data)

    def post(self, request):
        dicionario = json.loads(request.body)
        fruta = FrutaSerializer.pegar_fruta(dicionario["name"])

        if fruta.is_valid():
            fruta.save()
            return Response(fruta.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        fruta = Fruta.objects.all()
        if fruta:
            fruta.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class FrutaView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk):
        fruta = Fruta.objects.get(pk=pk)
        if fruta:
            serializer = FrutaSerializer(fruta)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        fruta = Fruta.objects.get(pk=pk)
        serializer = FrutaSerializer(fruta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        fruta = Fruta.objects.get(pk=pk)
        if fruta:
            fruta.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        