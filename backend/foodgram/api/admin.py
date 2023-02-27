from django.contrib import admin
from product.models import (
    Ingredients, Tags, Recipe,
    IngredRecipe, Subscriptions,
    ShoppingCart, Favorite
)

admin.site.register(Ingredients)
admin.site.register(Tags)
admin.site.register(Recipe)
admin.site.register(IngredRecipe)
admin.site.register(Subscriptions)
admin.site.register(ShoppingCart)
admin.site.register(Favorite)

class TagsAdmin(admin.AdminSite):
    prepopulated_fields = {"slug": ("name",)}