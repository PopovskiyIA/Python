# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.

from enum import Enum


class CarTurnDirection(Enum):
    LEFT = "на лево"
    RIGHT = "на право"


class CarType(Enum):
    TOWN_CAR = "городская машина"
    WORK_CAR = "рабочая машина"
    SPORT_CAR = "спортивная машина"
    POLICE_CAR = "полицейская машина"


class Car:
    speed: int
    color: str
    name: str
    type: CarType
    is_police: bool

    def __init__(self, speed, color, name, type, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.type = type
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} начала движение")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    @staticmethod
    def turn(direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.speed} км/ч")

    def info(self):
        print()
        print(
            f"Информация об автомобиле: цвет {self.color}, название {self.name}, тип {self.type.value}")
        self.show_speed()


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, CarType.TOWN_CAR, False)

    def show_speed(self):
        if self.speed > 60:
            print("Скорость движения автомобиля выше 60 км/ч")
        else:
            print(f"Текущая скорость {self.speed} км/ч")


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, CarType.WORK_CAR, False)

    def show_speed(self):
        if self.speed > 40:
            print("Скорость движения автомобиля выше 40 км/ч")
        else:
            print(f"Текущая скорость автомобиля {self.speed} км/ч")


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, CarType.SPORT_CAR, False)


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, CarType.POLICE_CAR, True)


# Тест
work_car = WorkCar(50, "красный", "Лада Ларгус")
work_car.info()

town_car = TownCar(70, "серый", "Газ Волга")
town_car.info()

sport_car = SportCar(10, "фиолетовый", "Лада гранта")
sport_car.info()
sport_car.turn(CarTurnDirection.LEFT.value)

police_car = PoliceCar(200, "белый", "Уаз Патриот")
police_car.info()
police_car.turn(CarTurnDirection.RIGHT.value)
