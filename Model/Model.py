import ipinfo
import json
import myipaddress as myip
from pyowm import OWM
from pyowm.utils.config import get_default_config
from Utility.Saver import Saver
from Utility.Forecast import Forecast
from datetime import datetime
from translate import Translator


class Model:
    def __init__(self, saver: Saver):
        self.forecast = None
        self.address = None
        self.client_ip = None
        self._model_observers = []
        self._saver = saver
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        self.translator = Translator(from_lang="english", to_lang="russian")
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

        self.forecast = Forecast(datetime.utcfromtimestamp(w.ref_time).astimezone(),
                                 self.address,
                                 w.detailed_status,
                                 int(w.temperature('celsius')['temp']),
                                 int(w.temperature('celsius')['feels_like']),
                                 w.wind()['speed'],
                                 )

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
        _address = self.handler.getDetails(self.client_ip).details['city']
        self.address = self.translator.translate(_address)

    def get_latest_forecasts(self, n):
        result = []
        try:
            with self._saver as s:
                ln = s.read(n)
                for el in ln:
                    result.append(Forecast(*el[1:]))
        except Exception as e:
            print(e)
            return e

        self.display = result
        self._notify_observers()

    def add_observer(self, inObserver):
        self._model_observers.append(inObserver)

    def remove_observer(self, inObserver):
        self._model_observers.remove(inObserver)

    def _notify_observers(self):
        for x in self._model_observers:
            x.model_is_changed()
