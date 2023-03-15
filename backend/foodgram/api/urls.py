from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    IngredientsViewSets, TagsViewSets, RecipeViewSets,
    UserViewSets
)

router = DefaultRouter()

router.register('ingredients', IngredientsViewSets)
router.register('tags', TagsViewSets)
router.register('recipes', RecipeViewSets)
router.register('users', UserViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path(r'auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
