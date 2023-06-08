from src.item import Item


class Mixin:
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value

    def change_lang(self, new_lang: str = 'RU'):
        if new_lang.lower() == 'en':
            self.__language = 'EN'
        elif new_lang.lower() == 'ru':
            self.__language = 'RU'
        else:
            raise AttributeError('AttributeError')
        return self


class KeyBoard(Item, Mixin):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        Mixin.__init__(self)

    def __str__(self):
        result = f"{self.name}"
        return result





