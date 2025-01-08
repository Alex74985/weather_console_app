def create_db_if_not_exist():

    import sqlite3

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('forecasts.db')
    cursor = connection.cursor()

    # Создаем таблицу Forecasts
    cursor.execute("CREATE TABLE IF NOT EXISTS Forecasts (id INTEGER PRIMARY KEY, dt DATETIME, location TEXT, status TEXT NOT NULL, temp INTEGER, temp_fl INTEGER,  wind INTEGER)")

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()