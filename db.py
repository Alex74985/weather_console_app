def create_db_if_not_exist():

    import sqlite3

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('forecasts.db')
    cursor = connection.cursor()

    # Создаем таблицу Forecasts
    cursor.execute("CREATE TABLE IF NOT EXISTS Forecasts (id INTEGER PRIMARY KEY, status TEXT NOT NULL, wind INTEGER, temp_max INTEGER, temp_min INTEGER, pressure INTEGER, visibility INTEGER, sunset TEXT, sunrise TEXT, location TEXT)")

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()