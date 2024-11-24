from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import InvestmentView, PortfolioView

urlpatterns = [
    path('investments/', InvestmentView.as_view(), name='add-investment'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
