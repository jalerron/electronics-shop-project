from src.item import Item


class Phone(Item):
    """
    Класс для представления телефона
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса телефон
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = value


    # def __setattr__(self, name, value):
    #     if name == "number_of_sim" and value <= 0:
    #         raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
    #     else:
    #         self.__dict__[name] = value