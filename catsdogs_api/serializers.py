from rest_framework import serializers

from main import models


class CatSerializer(serializers.Serializer):
    """Serializes a cat"""
    class Meta:
        model = models.Cat
        fields = ('id', 'animal_owner', 'cat_name', 'cat_bd')
        extra_kwargs = {'user_profile': {'read_only': True}}

class DogSerializer(serializers.Serializer):
    """Serializes a cat"""
    class Meta:
        model = models.Dog
        fields = ('id', 'animal_owner', 'dog_name', 'dog_bd')
        #extra_kwargs = {'user_profile': {'read_only': True}}