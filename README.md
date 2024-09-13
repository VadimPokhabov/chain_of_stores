# "Сеть по продаже электроники"

____

### Описание задачи:

* Создать веб-приложение с API-интерфейсом и админ-панелью.
* Создайте базу данных, используя миграции Django.
____

### Стек:

* Python 3.8+
* Django 3+
* DRF 3.10+
* PostgreSQL 10+

____
Для запуска проекта у себя локально необходимо:

1. git clone репозитория

```
https://github.com/VadimPokhabov/chain_of_stores.git
```

2. Установить виртуальное окружение venv

```
python3 -m venv venv для MacOS и Linux систем
python -m venv venv для windows
```

3. Активировать виртуальное окружение

```
source venv/bin/activate для MasOs и Linux систем
venv\Scripts\activate.bat для windows
```

4. установить файл с зависимостями

```
pip install -r requirements.txt
```

5. Создать базу данных в PgAdmin, либо через терминал. Необходимо дать название в файле settings.py в каталоге 'config' в
   константе (словаре) 'DATABASES'
6. Заполнить своими данными файл .env в корне вашего проекта. Образец файла лежит в корне .env.sample
7. Для запуска проекта использовать команду

```
python manage.py ruserver
```
____

### Импорт (восстановление) с loaddata

Команда loaddata позволяет загрузить фикстуры (экспортированные с помощью dumpdata данные). Синтаксис:

```
python manage.py loaddata db.json
```
----
В файле db2.json исключены таблицы contenttypes и auth.permissions

```commandline
python manage.py loaddata db2.json
```