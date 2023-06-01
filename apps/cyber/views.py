from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ComputerSessionSerializer
from .models import ComputerSession
from rest_framework.permissions import IsAuthenticated

class ComputerSessionView(viewsets.ModelViewSet):
    """Viewset for the ComputerSession model."""
    serializer_class = ComputerSessionSerializer
    queryset = ComputerSession.objects.all()
    permission_classes = [IsAuthenticated]  # Only authenticated users can interact with the sessions