from View.View import View


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
        menu = {1: self.get_weather,
                2: self.set_address,
                3: self.get_latest_forecasts,
                4: self.close}
        try:
            key = int(key)
            if key in menu.keys():
                menu[key]()
            else:
                raise ValueError
        except ValueError:
            self.mView.print_exec(f"Введите пункт меню целым числом")
            self.mModel.menu()

    def _start(self):
        self.mModel.menu()
        while self.running:
            self._on_press(input())

    def close(self):
        self.running = False



