class Forecast:
    def __init__(self, status, wind, temp_max, temp_min, pressure, visibility, sunset, sunrise, location):
        self._status = status
        self._wind = wind
        self._temp_max = temp_max
        self._temp_min = temp_min
        self._pressure = pressure
        self._visibility = visibility
        self._sunset = sunset
        self._sunrise = sunrise
        self._location = location

    def __repr__(self):
        return f'\n-----------------------\n' \
               f'Погода: {self._status}\n' \
               f'Скорость ветра: {self._wind}\n' \
               f'Максимальная температура: {self._temp_max}\n' \
               f'Минимальная температура: {self._temp_min}\n' \
               f'Атмосферное давление: {self._pressure}\n' \
               f'Видимость: {self._visibility}\n' \
               f'Восход: {self._sunrise}\n' \
               f'Закат: {self._sunset}\n' \
               f'Место: {self._location}\n' \
               f'-----------------------\n'

    def values(self) -> tuple:
        return tuple([self._status,
                      self._wind,
                      self._temp_max,
                      self._temp_min,
                      self._pressure,
                      self._visibility,
                      self._sunset,
                      self._sunrise,
                      self._location])
