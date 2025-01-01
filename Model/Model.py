import datetime

import ipinfo
import json
import myipaddress as myip
from pyowm import OWM
from Utility.Saver import Saver
from Utility.Forecast import Forecast


class Model:
    def __init__(self, saver: Saver):
        self.forecast = None
        self.address = None
        self.client_ip = None
        self._mObservers = []
        self._saver = saver
        with open('api.json', 'r') as file:
            api_data = json.load(file)
            self.wm = OWM(api_data['OpenWeather api key']).weather_manager()
            self.handler = ipinfo.getHandler(api_data['IP_info key'])

        self.display = None

    def menu(self):
        self.display = "1. Погоду по месту\n2. Погода в городе\n3. Последние прогнозы\n4. Выход"
        self._notify_observers()

    def get_weather(self):

        if not self.address:
            self._get_client_address()

        observation = self.wm.weather_at_place(self.address)
        w = observation.weather

        # self.content = {'status': w.detailed_status,
        #                 'wind': w.wind()['speed'],
        #                 'temp_max': int(w.temperature('celsius')['temp_max']),
        #                 'temp_min': int(w.temperature('celsius')['temp_min']),
        #                 'pressure': w.barometric_pressure()['press'],
        #                 'visibility': w.visibility(),
        #                 'sunset': str(w.sunset_time('date').astimezone().time()),
        #                 'sunrise': str(w.sunset_time('date').astimezone().time()),
        #                 'dt': str(datetime.datetime.now().astimezone())}

        self.forecast = Forecast(w.detailed_status,
                                 w.wind()['speed'],
                                 int(w.temperature('celsius')['temp_max']),
                                 int(w.temperature('celsius')['temp_min']),
                                 w.barometric_pressure()['press'],
                                 w.visibility(),
                                 str(w.sunset_time('date').astimezone().time()),
                                 str(w.sunset_time('date').astimezone().time()),
                                 self.address)

        self.display = self.forecast
        self._notify_observers()

        try:
            with self._saver as s:
                s.save(self.forecast)
        except Exception as e:
            return print(e)

    def set_address(self, s):
        self.address = s

    def _get_client_address(self):
        self.client_ip = myip.public_ip()
        self.address = self.handler.getDetails(self.client_ip).details['city']

    def get_latest_forecasts(self, n):
        result = []
        try:
            with self._saver as s:
                ln = s.read(n)
                for el in ln:
                    result.append(Forecast(*el[1:]))
        except Exception as e:
            return e

        self.display = result
        self._notify_observers()

    def add_observer(self, inObserver):
        self._mObservers.append(inObserver)

    def remove_observer(self, inObserver):
        self._mObservers.remove(inObserver)

    def _notify_observers(self):
        for x in self._mObservers:
            x.model_is_changed()
