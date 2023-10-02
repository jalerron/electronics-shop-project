from accessify import private, protected
import csv


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

    @classmethod
    def instantiate_from_csv(cls, filename: str):
        """
        Инициализируем экземпляры класса из файла item.csv
        """
        with open(filename, 'r', newline='') as file:
            data = csv.DictReader(file)
            items = []
            for data_ in data:
                name = data_['name']
                price = float(data_['price'])
                quantity = int(data_['quantity'])
                item = cls(name, price, quantity)
                items.append(item)

            cls.all = items

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

# item1 = Item("СуперСмартфон", 10000, 5)
# item1.name = 'СуперСмартфон'
#
#
# Item.instantiate_from_csv('items.csv')
# print(len(item1.name))
# print(Item.data)
