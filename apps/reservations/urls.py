from django.urls import path
from .views import TarifaView

urlpatterns = [
    path('', TarifaView.as_view({'get': 'list', 'post': 'create'}), name='tarifas'),
    path('<int:pk>/', TarifaView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='tarifa'),
]