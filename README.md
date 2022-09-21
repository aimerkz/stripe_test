# Тестовое задание Stripe API

Тестовый проект по использованию фреймворка Django и API сервиса приема платежей [Stripe](https://stripe.com/).

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

## Установка
 - Клонируйте репозиторий на свою локальную машину:
```sh
git clone https://github.com/aimerkz/stripe_test.git
```
 - Перейдите в папку infra:
```sh
cd infra
```
 - Создайте файл с переменными окружения:
```sh
 Пример есть в файле .env.example
```
 - Запустите docker:
```sh
docker-compose up -d
```
- Выполните миграции:
```sh
docker-compose exec web python manage.py migrate
```
- Заполните базу тестовыми данными:
```sh
docker-compose exec web python manage.py loaddata infra/dump.json
```
 - Список доступных маршрутов:
```sh
127.0.0.1:8000/item/{id} - получение html страницы выбранного Item
127.0.0.1:8000/buy/{id} - получение Stripe Session Id для оплаты выбранного Item
127.0.0.1:8000/buy_order/{id} -  получение Stripe Session Id для оплаты выбранного Order
```
 - Документация к API: \
[Swagger-ui](http://127.0.0.1:8000/swagger/)
