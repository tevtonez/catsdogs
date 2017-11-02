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

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(animal_owner=self.request.user)


class DogViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating users Dogs."""

    serializer_class = serializers.DogSerializer
    queryset = models.Dog.objects.all()
    permission_classes = (permissions.UpdateOwnAnimal, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(animal_owner=self.request.user)

