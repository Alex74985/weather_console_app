from db import create_db_if_not_exist


from Model.Model import Model
from Controller.Controller import Controller
from Utility.Saver import SQLiteSaver


def main():
    model = Model(SQLiteSaver())
    controller = Controller(model)


if __name__ == "__main__":
    create_db_if_not_exist()
    main()
