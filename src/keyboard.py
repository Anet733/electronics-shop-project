from src.item import Item


class Mixin:
    language = "EN"

    def __str__(self):
        result = f"{self.language}"
        return result

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        else:
            raise AttributeError()
        return self


class KeyBoard(Mixin, Item):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __str__(self):
        result = f"{self.name}"
        return result





