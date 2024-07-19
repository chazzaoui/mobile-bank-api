from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import random

class PortfolioValueView(APIView):
    def get(self, request, format=None):
        value = random.uniform(10000, 50000)
        value_with_dollar = f"${value:,.2f}"
        return Response({'portfolio_value': value_with_dollar})
