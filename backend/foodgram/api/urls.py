from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import IngredientsViewSets


router = DefaultRouter()

router.register('ingredients', IngredientsViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
