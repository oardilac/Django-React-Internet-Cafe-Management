from rest_framework import serializers
from .models import ComputerSession

class ComputerSessionSerializer(serializers.ModelSerializer):
    """Serializer for the ComputerSession model."""
    class Meta:
        model = ComputerSession
        fields = '__all__'