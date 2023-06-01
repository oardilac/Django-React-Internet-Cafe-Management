from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CustomTokenObtainPairView, LogoutView

app_name = "accounts"

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_login'),
    path('logout/', LogoutView.as_view(), name='token_logout'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]