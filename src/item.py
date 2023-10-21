import csv
import os.path
from pathlib import Path

ROOT = Path(__file__).parent
DATA_PATH = Path.joinpath(ROOT, 'items.csv')
path = DATA_PATH


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    data = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)  # Добавляем созданный экземпляр в атрибут класса

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализируем экземпляры класса из файла item.csv
        """
        if os.path.exists(path):
            with open(path, 'r', newline='') as file:
                data = csv.DictReader(file)
                items = []
                if len(data.fieldnames) < 3:
                    raise InstantiateCSVError('Файл item.csv поврежден')
                else:
                    for data_ in data:
                        name = data_['name']
                        price = float(data_['price'])
                        quantity = int(data_['quantity'])
                        item = cls(name, price, quantity)
                        items.append(item)

                cls.all = items
        else:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(str_number: str):
        """
        Возвращает из строки число в int
        """
        number = str_number.split('.')
        return int(number[0])

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


class InstantiateCSVError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
