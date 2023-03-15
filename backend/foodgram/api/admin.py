from django.contrib import admin
from product.models import (
    Ingredients, Tags, Recipe,
    IngredRecipe,
    ShoppingCart, Favorite
)


class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    prepopulated_fields = {"slug": ("name",)}


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author')
    search_fields = ('ingredients',)


admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredRecipe)
admin.site.register(ShoppingCart)
admin.site.register(Favorite)
