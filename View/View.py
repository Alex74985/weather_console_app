from Utility.Observer import Observer


class View(Observer):
    def __init__(self, inController, inModel):
        self.mController = inController
        self.mModel = inModel

        self.mModel.add_observer(self)

    def model_is_changed(self):
        # print("\033[H\033[J", end="")
        if isinstance(self.mModel.display, list):
            print(*self.mModel.display, sep='\n')
        else:
            print(self.mModel.display)

    def ask_n(self):
        n = int(input('\nВведите количесвто записей для отображения - '))
        return n

    def ask_address(self):
        s = input('\nВведите название города - ')
        return s

    def print_exec(self, s):
        print(s)

