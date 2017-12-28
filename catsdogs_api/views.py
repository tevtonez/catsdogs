from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from main import models
from . import permissions


class CatViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating users Cats."""

    serializer_class = serializers.CatSerializer
    queryset = models.Cat.objects.all()
    permission_classes = (permissions.UpdateOwnAnimal, IsAuthenticated)



class DogViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating users Dogs."""

    serializer_class = serializers.DogSerializer
    queryset = models.Dog.objects.all()
    permission_classes = (permissions.UpdateOwnAnimal, IsAuthenticated)

