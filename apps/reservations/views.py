from rest_framework import viewsets
from .models import Tarifa
from .serializers import TarifaSerializer
from rest_framework.permissions import IsAuthenticated

class TarifaView(viewsets.ModelViewSet):
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer
    permission_classes = [IsAuthenticated]