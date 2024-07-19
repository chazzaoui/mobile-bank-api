from django.urls import path
from .views import PortfolioValueView

urlpatterns = [
    path('value/', PortfolioValueView.as_view(), name='portfolio-value'),
]