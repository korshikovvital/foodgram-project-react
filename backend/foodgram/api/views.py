from rest_framework import viewsets
from api.serializer import IngredientsSerializer
from product.models import Ingredients


class IngredientsViewSets(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer