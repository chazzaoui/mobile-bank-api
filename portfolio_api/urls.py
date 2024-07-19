from django.contrib import admin
from django.urls import path, include
from portfolio.views import PortfolioValueView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('portfolio.urls')),
    path('', PortfolioValueView.as_view(), name='portfolio-value'),
]