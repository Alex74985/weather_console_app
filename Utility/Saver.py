import pytz
from typing import Protocol
import sqlite3
from pathlib import Path
import os


class Saver(Protocol):
    def read(self, n):
        pass

    def save(self, data):
        pass


class SQLiteSaver:
    # def __init__(self):
    #     self._connection()

    def save(self, data):
        self.cursor.execute('INSERT INTO FORECASTS (status, wind, temp_max, temp_min, pressure, visibility, sunset, sunrise, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', data.values())

    def read(self, n):
        self.cursor.execute("SELECT * FROM FORECASTS ORDER BY 'id' DESC ")
        last_n = self.cursor.fetchmany(n)
        return last_n

    def _connection(self):
        BASE_DIR = Path(__file__).resolve().parents[1]
        db_path = os.path.join(BASE_DIR, 'forecasts.db')

        try:
            self.connection = sqlite3.connect(db_path)
            self.cursor = self.connection.cursor()
        except Exception as e:
            return e

    def __enter__(self):
        self._connection()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
