from ..models import Fruta
from rest_framework import serializers

class FrutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruta
        fields = '__all__'