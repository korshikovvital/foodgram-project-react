#FOODGRAM

# Описание:
«Продуктовый помощник»: сайт, на котором пользователи будут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.


Клонировать репозиторий и перейти в папку backend:
<<https://github.com/korshikovvital/foodgram-project-react.git>>

IP: 62.84.123.253
admin 'vit' password '1234'


Создать и активировать виртуальное окружение:

`python -m venv venv
source venv/Scripts/activate`

Установить зависимости из файла requirements.txt:

`pip install -r requirements.txt`

Перейти в папку foodgram и выполнить миграции:

`cd foodgram/
python manage.py migrate`

Запустить проект

`python manage.py runserver`


Стек технологий
Python 3, Django 2.2, Django REST framework, PostgreSQL, Djoser


Автор проекта:
Коршиков Виталий 
