# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу
# метода.


class Road:
    _length: int
    _width: int

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_the_mass_of_asphalt(self, asphalt_square_meter_weight, road_thickness):
        try:
            square_meter_weight = int(asphalt_square_meter_weight)
            thickness = int(road_thickness)
            return self._length * self._width * square_meter_weight * thickness
        except ValueError:
            print("Road.calculate_the_mass_of_asphalt - illegal argument passed to method")
            return 0


# Тест
try:
    road_length = int(input("Введите длину дороги в метрах: "))
    road_width = int(input("Введите ширину дороги в метрах: "))
    asphalt = input("Введите массу асфальта для покрытия одного кв метра дороги асфальтом (в килограммах): ")
    roadway_thickness = input("Введите толщину дорожного полотна в сантиметрах: ")
    road = Road(road_length, road_width)
    asphalt_mass = road.calculate_the_mass_of_asphalt(asphalt, roadway_thickness)
    print(f"Масса асфальта, необходимого для покрытия всего дорожного полотна равна {asphalt_mass} кг")
except ValueError:
    print("Введены некорректные данные")
