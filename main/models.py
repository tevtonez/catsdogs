from django.db import models
from django.contrib.auth.models import User

class Cat(models.Model):

    cat_name = models.CharField(null=True, blank=False, max_length=50)
    cat_bd = models.DateField(null=True, blank=False)
    animal_owner = models.ForeignKey('auth.User', null=True, blank=False, on_delete=models.CASCADE, related_name='cat_owner')

    class Meta:
        verbose_name = "Cat"
        verbose_name_plural = "Cats"

        permissions=(
            ('read_item', 'Can read item'),
        )

    def __str__(self):
        return self.cat_name


class Dog(models.Model):

    dog_name = models.CharField(null=True, blank=False, max_length=50)
    dog_bd = models.DateField(null=True, blank=False)
    animal_owner = models.ForeignKey('auth.User', null=True, blank=False, on_delete=models.CASCADE, related_name='dog_owner')

    class Meta:
        verbose_name = "Dog"
        verbose_name_plural = "Dogs"

    def __str__(self):
        return self.dog_name

