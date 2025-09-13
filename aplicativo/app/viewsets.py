import json
from ..models import Fruta
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..app.serializer import FrutaSerializer

class FrutaView(APIView):
    def get(self, request):
        frutas = Fruta.objects.all()
        serializer = FrutaSerializer(frutas, many=True)
        return Response(serializer.data)
    
    def post(self, request)