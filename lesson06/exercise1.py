# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time

from enum import Enum


class TrafficLightColor(Enum):
    RED = "красный"
    YELLOW = "жёлтый"
    GREEN = "зелёный"


traffic_light_time_configuration = {TrafficLightColor.RED: 7, TrafficLightColor.YELLOW: 2, TrafficLightColor.GREEN: 10}


class TrafficLight:
    __color: TrafficLightColor

    def __init__(self):
        self.__color = TrafficLightColor.GREEN

    def __change_light_color(self, new_color):
        self.__color = new_color
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"Включен {self.__color.value} цвет светофора в {current_time}")
        time.sleep(traffic_light_time_configuration[new_color])

    def running(self, running_time_in_seconds):
        start_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"Светофор включен в {start_time}")
        total_time = time.time() + running_time_in_seconds
        while total_time > time.time():
            if self.__color is TrafficLightColor.RED:
                self.__change_light_color(TrafficLightColor.YELLOW)
            elif self.__color is TrafficLightColor.YELLOW:
                self.__change_light_color(TrafficLightColor.GREEN)
            elif self.__color is TrafficLightColor.GREEN:
                self.__change_light_color(TrafficLightColor.RED)
            else:
                print(f"Некорректный цвет светофора: {self.__color}. Выполнение программы будет прервано")
                exit(1)
        end_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"Светофор выключен в {end_time}")


# Тест
try:
    running_time = int(input("Введите время работы светофора в секундах:"))
    if running_time > 0:
        traffic_light = TrafficLight()
        traffic_light.running(running_time)
    else:
        print("Время работы светофора в секундах должно быть положительным числом")
except ValueError:
    print("Некорректное значение времени работы светофора в секундах")

