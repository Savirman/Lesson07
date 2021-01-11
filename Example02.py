"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod

class AbstractClothes(ABC):
    name: str
    @abstractmethod
    def rashod(self):
        pass

    def show_name(self, name: str):
        self.name = name
        print(self.name)

class Coat(AbstractClothes):
    def __init__(self, size):
        self.size = size

    @property
    def rashod(self, size):
        rash = (size / 6.5 + 0.5)
        return rash

class Suit(AbstractClothes):
    def __init__(self, height):
        self.height = height

    def rashod(self, height):
        rash = (2 * height + 0.3)
        return rash

coat = Coat(48)
suit = Suit(176)

coat.name = "Coat"
suit.name = "Suit"

print(coat.rashod(coat.size))
print(suit.rashod(suit.height))
total_ras = coat.rashod(coat.size) + suit.rashod(suit.height)
print(f"Общий расход ткани {total_ras}")
