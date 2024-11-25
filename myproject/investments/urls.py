from django.urls import path
from .views import InvestmentView, PortfolioView

urlpatterns = [
    path('create_investments/', InvestmentView.as_view(), name='add-investment'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
]
