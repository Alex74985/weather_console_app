import sys

from View.View import View
from pynput import keyboard


class Controller:
    def __init__(self, inModel):
        self.mModel = inModel
        self.mView = View(self, self.mModel)
        self.running = True

        self._start()

    def set_address(self):
        s = self.mView.ask_address()

        self.mModel.set_address(s)
        self.get_weather()

    def get_weather(self):
        try:
            self.mModel.get_weather()
        except Exception as e:
            self.mView.print_exec("Нет данных о локации")
            self.mModel.address = None
        self.mModel.menu()

    def get_latest_forecasts(self):

        try:
            n = int(self.mView.ask_n())
            self.mModel.get_latest_forecasts(n)
        except ValueError:
            self.mView.print_exec("Введите целое число")

        self.mModel.menu()

    def _on_press(self, key):
        # print(type(key), key)
        menu = {1: self.get_weather,
                2: self.set_address,
                3: self.get_latest_forecasts,
                4: self.close}
        try:
            # if key == keyboard.Key.esc:
            #     return False
            if key in menu.keys():
                menu[key]()
        except AttributeError as e:
            self.mView.print_exec(f"Неверный ввод")
            self.mModel.menu()

    def _start(self):
        self.mModel.menu()
        while self.running:
            self._on_press(int(input()))
            # self.mView.start()
            # with keyboard.Listener(on_press=self._on_press) as listener:
            #     listener.join()

    def close(self):
        self.running = False



