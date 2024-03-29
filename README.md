## api_final

**Описание:**

Проект API_Yatube выполняет запросы на различные эндоинты. 

**Примеры:**

Запросы осуществялются к 4 эндоинтам не считая запросов к эндоинтам бибилиотеки djoser. 

```
К posts(обрабатывает все запросы и доступен всем пользователям с разной степенью прав)
К groups(обрабатывает только безопасные запросы, создавать может только администратор)
К follow(обрабатывает только запросы аутентифицированных пользователей GET и POST)
К posts/{pk}/comments(обрабаывает запросы к комментариям конкретного поста для всех пользователей с разной степенью прав)
```

**Несколько примеров запросов к эндоинтам:**

http://127.0.0.1:8000/api/v1/posts/ - GET запрос для получения списка постов

```
 "count": 123,
 "next": "http://api.example.org/accounts/?offset=400&limit=100",
 "previous": "http://api.example.org/accounts/?offset=200&limit=100",
 "results": [
       {
         "id": 0,  
         "author": "string",
         "text": "string",
         "pub_date": "2021-10-14T20:41:29.648Z",
         "image": "string",
         "group": 0
 }
 ]
 }
```

http://127.0.0.1:8000/api/v1/posts/ - POST Запрос 
```
{
 "text": "string",
 "image": "string",
 "group": 0
}
```

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/- Post запрос

```
{
  "text": "string"
}
```
**Как запустить проект:**

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/api_final_yatube.git
cd yatube_api
```

2. Cоздать и активировать виртуальное окружение:

```
python -m venv env
source venv/Script/activate
```

3. Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Выполнить миграции:

```
python manage.py migrate
```

5.Запустить проект:

```
python manage.py runserver
```
