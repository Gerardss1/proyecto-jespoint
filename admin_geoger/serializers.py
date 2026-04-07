from rest_framework import serializers
from .models import direccion

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = direccion
        fields = "__all__"