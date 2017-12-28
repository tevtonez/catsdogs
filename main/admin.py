from django.contrib import admin
from . import models


class CatAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return models.Cat.objects.filter(animal_owner=request.user)

    def has_add_permission(self, request):
        return True
    def has_change_permission(self, request, obj=None):
        return True
    def has_module_permission(self, request):
        return True


class DogAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True
    def has_change_permission(self, request, obj=None):
        return True
    def has_module_permission(self, request):
        return True

    def get_queryset(self, request):
        return models.Cat.objects.filter(animal_owner=request.user)


admin.site.register(models.Cat, CatAdmin)
admin.site.register(models.Dog, DogAdmin)


