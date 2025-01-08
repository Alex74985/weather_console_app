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

    def save(self, data):
        self.cursor.execute('INSERT INTO FORECASTS (dt, location, status, temp, temp_fl, wind) VALUES (?, ?, ?, ?, ?, ?)', data.values())

    def read(self, n):
        self.cursor.execute("SELECT * FROM FORECASTS ORDER BY id DESC LIMIT (?)", (n, ))
        last_n = self.cursor.fetchall()
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
