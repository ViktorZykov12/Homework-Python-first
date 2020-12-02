from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, size, growth):
        self.name = name
        self.size = size
        self.growth = growth

    def __str__(self):
        return f'Для пошива {self.name} необходимо {self.count} м ткани'

    def __add__(self, other):
        return f'Всего необходимо {self.count + other.count} м ткани'

    @abstractmethod
    def count(self):
        pass


class Coat(Clothes):
    @property
    def count(self):
        return round(self.size / 6.5 + 0.5, 2)


class Costume(Clothes):
    @property
    def count(self):
        return round(2 * self.growth + 0.3, 2)


coat = Coat('Пальто', 54, 1.74)
costume = Costume('Костюм', 54, 1.74)
print(coat)
print(costume)
print(coat + costume)