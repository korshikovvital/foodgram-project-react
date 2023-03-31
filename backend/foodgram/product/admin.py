from django.contrib import admin

from product.models import (Favorite, Ingredients, IngredRecipe, Recipe,
                            ShoppingCart, Tags)


class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    prepopulated_fields = {"slug": ("name",)}


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)


class IngredientsInline(admin.TabularInline):
    model = IngredRecipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'favorite_count')
    list_filter = ('name', 'author', 'tags',)
    search_fields = ('ingredients',)
    inlines = [
        IngredientsInline,
    ]

    def favorite_count(self, obj):
        return obj.favorits.count()


admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredRecipe)
admin.site.register(ShoppingCart)
admin.site.register(Favorite)
