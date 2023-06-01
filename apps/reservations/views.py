from rest_framework import viewsets
from .models import Tarifa
from .serializers import TarifaSerializer

class TarifaView(viewsets.ModelViewSet):
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer