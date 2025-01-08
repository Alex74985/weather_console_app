class Forecast:
    def __init__(self, time, location, status, temp, feels_like, wind):
        self._location = location
        self._status = status
        self._temp = temp
        self._feels_like = feels_like
        self._wind = wind
        self._time = time

    def __repr__(self):
        return f'Текущее время: {self._time}\n'\
               f'Название города: {self._location}\n' \
               f'Погода: {self._status}\n' \
               f'Текущая температура: {self._temp} градусов по цельсию\n' \
               f'Ощущается как: {self._feels_like} градусов по цельсию\n' \
               f'Скорость ветра: {self._wind} м/с\n'

    def values(self) -> tuple:
        return tuple([self._time,
                      self._location,
                      self._status,
                      self._temp,
                      self._feels_like,
                      self._wind,
                      ])
