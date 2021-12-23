# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У
# этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
# 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода
# ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    name: str
    value: int

    def __init__(self, name, value):
        self.name = name
        self.value = value

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):

    @property
    def fabric_consumption(self):
        return round(self.value / 6.5 + 0.5, 2)

    def __str__(self):
        return f"Расход ткани для пальто «{self.name}» с размером {self.value} составит {self.fabric_consumption}"


class Suit(Clothes):

    @property
    def fabric_consumption(self):
        return 2 * self.value + 0.3

    def __str__(self):
        return f"Расход ткани для костюма «{self.name}» на рост {self.value} составит {self.fabric_consumption}"


# Тест
gentleman = Coat("Джентельмен", 40)
print(gentleman)

romantic = Suit("Романтик", 180)
print(romantic)
