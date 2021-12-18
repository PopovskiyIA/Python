# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисует ручка {self.title}")


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Пишет карандаш {self.title}")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Красит маркер {self.title}")


# Тест
test = Stationery("none")
test.draw()
print()

test = Pencil("Bic")
test.draw()
print()

test = Pen("Stabilo")
test.draw()
print()

test = Handle("Edding")
test.draw()
