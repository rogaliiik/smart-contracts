from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from .serializers import TokenSerializer
from .models import Token


class TokenAPICreate(CreateAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


class TokenAPIList(ListAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


# class TokenAPITotal(ListAPIView):
#     queryset = Token.objects.all().count()
#     serializer_class = TokenSerializer