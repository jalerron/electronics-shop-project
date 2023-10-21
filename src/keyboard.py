from src.item import Item


class MixinLang:
    """
    Класс миксин для языка клавиатуры
    """

    def __init__(self):
        """
        Инициализация класса
        """
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Item, MixinLang):

    def __init__(self, name, price, quantity) -> None:
        """
        Инициализация класса Keyboard
        """
        super().__init__(name, price, quantity)
        MixinLang.__init__(self)
