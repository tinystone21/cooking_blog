## ТЕСТОВОЕ ЗАДАНИЕ
***
# Как запустить проект? 

1.  Открыть терминал или консоль и перейти в директорию проекта.
2.  Создать виртуальное окружение `python3 -m venv venv`
3.  Установить зависимости коммандой `pip install -r requirements.txt`
4.  Создать базу данных `postgres`
5.  Установить переменное окружение:
    * Перейти в директорию `.envs`
    * Создать файл `.env`
    * Ввести данные от своего `postgres`
    * Ввести `SECRET_KEY` от проекта
6.  Выполнить комманды:
    * `python3 manage.py makemigrations`
    * `python3 manage.py migrate`
    * `python3 manage.py runserver`
