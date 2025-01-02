Порядок действий для запуска:
-
1. Установить python 3.12
2. В корневой папке проекта выполнить:
- python -m venv venv
3. Для Windows: 
- venv\Scripts\activate
3. Для Linux/MacOs:
- venv/bin/acivate
4. В корневой папке проекта выполнить:
- pip install -r requirements.txt
5. Запустить main.py

P.S. Если возникает ошибка 'AttributeError: module 'pkgutil' has no attribute 'ImpImporter'. Did you mean: 'zipimporter'?'
Выполните команды:
- python -m ensurepip --upgrade
- python -m pip install --upgrade setuptools 
