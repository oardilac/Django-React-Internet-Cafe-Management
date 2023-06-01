from django.urls import path
from .views import PagoView

urlpatterns = [
    path('', PagoView.as_view({'get': 'list', 'post': 'create'}), name='pagos'),
    path('<int:pk>/', PagoView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='pago'),
]