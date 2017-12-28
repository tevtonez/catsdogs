from rest_framework.routers import DefaultRouter

from django.conf.urls import include
from django.conf.urls import url

from . import views


app_name = 'catsdogs_api'


router = DefaultRouter()
router.register('cats', views.CatViewSet)
router.register('dogs', views.DogViewSet)

urlpatterns=[
    url(r'', include(router.urls)),
    url(r'^cat/$', views.CatViewSet, name='api_cat'),
    url(r'^dog/$', views.DogViewSet, name='api_dog'),

]
