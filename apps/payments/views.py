from rest_framework import viewsets
from .models import Pago
from .serializers import PagoSerializer
from rest_framework.permissions import IsAuthenticated

class PagoView(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]