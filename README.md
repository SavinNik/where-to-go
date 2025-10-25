# Where to Go

Проект на Django для отображения интересных мест на карте.

Попробовать можно тут -> [https://where-to-go-7rm7.onrender.com/](https://where-to-go-7rm7.onrender.com/)

## Начало работы

### Создание виртуального окружения

```bash
python -m venv venv
```

### Активация виртуального окружения

Для Linux/MacOS:
```bash
source venv/bin/activate
```

Для Windows:
```bash
venv\Scripts\activate
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Настройка переменных окружения

Создайте файл `.env` в корневой директории проекта и заполните его по примеру:

```
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### Создание базы данных

1. Убедитесь, что у вас установлен PostgreSQL
2. Создайте новую базу данных:
```bash
createdb your_db_name
```

### Применение миграций

```bash
python manage.py migrate
```

### Создание суперпользователя

```bash
python manage.py createsuperuser
```
Админка доступна по адресу: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### Импорт данных из JSON

Для загрузки данных из JSON-файлов в базу данных выполните:

```bash
python manage.py import_places путь/к/директории/с/json-файлами
```

### Запуск сервера разработки

```bash
python manage.py runserver
```

После запуска сервера приложение будет доступно по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Структура проекта

- `where_to_go/` - основные настройки проекта
- `places/` - приложение с основной логикой
- `static/` - статические файлы (CSS, JavaScript, изображения)
- `templates/` - HTML-шаблоны
- `media/` - загружаемые файлы

## Используемые технологии

- Python 3.x
- Django
- PostgreSQL
- Django Admin Sortable2
- TinyMCE
- Pillow для работы с изображениями