from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()


class Ingredients(models.Model):
    """Модель ингредиентов"""
    name = models.CharField('Продукт', max_length=120)
    measurement_unit = models.CharField(
        'Единица измерения', max_length=120
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.name}-{self.measurement_unit}'


class Tags(models.Model):
    """Модель тегов"""
    name = models.CharField('Имя тега', max_length=120)
    color = models.CharField('Цвет', max_length=120, help_text='RGB')
    slug = models.SlugField('Адрес', max_length=120, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Модель рецетов"""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='recipes', verbose_name='Автор'
    )
    name = models.CharField('Название', max_length=200)
    tags = models.ManyToManyField(
        Tags, related_name='recipes', verbose_name='Тэг'
    )
    image = models.ImageField('Картинка', upload_to='media/')
    text = models.TextField('Описание')
    cooking_time = models.IntegerField(
        'Время приготовления',
        validators=[MinValueValidator(limit_value=1, message='Не менее 1')]
    )
    ingredients = models.ManyToManyField(
        Ingredients, through='IngredRecipe', related_name='recipes'
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredRecipe(models.Model):
    name = models.ForeignKey(
        Ingredients, on_delete=models.CASCADE,
        related_name='ingreds', verbose_name='Название ингридиента'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name='recipe', verbose_name='Рецепт'
    )
    amount = models.PositiveSmallIntegerField('Количество')


class Subscriptions(models.Model):
    """Подписка"""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор', related_name='following'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Пользователь', related_name='follow'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class ShoppingCart(models.Model):
    """Список продуктов"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Пользователь', related_name='carts'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        verbose_name='Рецепт', related_name='recipes'
    )

    class Meta:
        verbose_name = 'Список покупки'
        verbose_name_plural = 'Список покупок'


class Favorite(models.Model):
    """Избранные рецепты"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Пользователь', related_name='favorit'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        verbose_name='Рецепт', related_name='favorits'
    )

    class Meta:
        verbose_name = 'Избраный'
        verbose_name_plural = 'Избранные'
