# tt_cook_book
Поварская книга (тестовое задание)
## Функционал
Приложение позволяет производить следующие действия:
1. Добавление к рецепту ингредиента с указанием необходимого количества.
2. Изменение количества приготовленных блюд для кажлого ингредиента, входящего в рецепт.
3. Вывод списка рецептов, в которых заданный ингредиент отсутствует  или входит в количестве менее 10 грамм.
## Используемые технологии
UBUNTU, PostgreSQL, PYTHON, Django, Docker
## Развёртывание системы
1. Склонировать репозиторий:
```
$ git clone git@github.com:Katsmannn/tt_cook_book.git
```
2. Зайти в каталог проекта
```
$ cd tt_cook_book/
```
3. Создать файл с параметрами подключения к БД:
```
$ nano .env
```
Файл должен содержать параметры:
```
DB_NAME=# имя базы данных
DB_HOST=# хост базы данных
DB_USER=# пользователь PostgreSQL
DB_PASSWORD=# пароль PostgreSQL

```
4. Собрать и запустить Docker контейнеры с бд и приложением:
```
$ sudo docker-compose build
$ sudo docker-compose up -d
```
5. Выполнить миграции:
```
$ sudo docker-compose exec web python3 manage.py makemigrations
$ sudo docker-compose exec web python3 manage.py makemigrations recipes
$ sudo docker-compose exec web python3 manage.py migrate
```
6. Создать суперпользователя для использования админ  панели:
```
$ sudo docker-compose exec web python3 manage.py createsuperuser
```
7. Заполнить базу данных данными:
```
$ sudo docker-compose exec web python3 manage.py create_data_in_db
```
Данные для заполнения находятся в файлах `DATA/ingredients.csv` - список ингредиентов, `DATA/recipes.txt` - список рецептов

Доступные эндпоинты:  
-- добавление ингредиента `<product_id>` к рецепту `<recipe_id>`
```
127.0.0.1:8000/recipes/<recipe_id>/edit/?product_id=<product_id>&weight=...
```
-- увеличение на 1 количества приготовлений рецепта `<recipe_id>`
```
127.0.0.1:8000/recipes/<recipe_id>/cook/
```
-- получение списка рецептов, в которых отсутствует (или почти отсутствует) ингредиент `<product_id>`
```
127.0.0.1:8000/recipes/without_product/<product_id>/
```
-- панель администратора
```
127.0.0.1:8000/admin/
```

![](https://img.shields.io/github/languages/count/katsmannn/tt_cook_book)