from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    equipment_type: str
    size: int

    def __init__(self, equipment_type: str, size: int):
        self.equipment_type = equipment_type
        self.size = size


class Printer(OfficeEquipment):
    color_printer: bool

    def __init__(self, color_printer: bool, size: int):
        super().__init__("Printer", size)
        self.color_printer = color_printer

    @staticmethod
    def print(value):
        print(f'Printing incoming value {value}')


class Scanner(OfficeEquipment):
    fast_scan: bool

    def __init__(self, fast_scan: bool, size: int):
        super().__init__("Scanner", size)
        self.fast_scan = fast_scan

    @staticmethod
    def scan(value):
        print(f'Scanning incoming value {value}')


class Copier(OfficeEquipment):
    color_copier: bool

    def __init__(self, color_copier: bool, size: int):
        super().__init__("Copier", size)
        self.color_copier = color_copier

    @staticmethod
    def copy(value):
        print(f'Copying incoming value {value}')


class Warehouse:
    total_size: int
    current_size: int
    stored_equipment: dict

    def __init__(self, total_size: int):
        self.total_size = total_size
        self.current_size = 0
        self.stored_equipment = {"Printer": 0, "Scanner": 0, "Copier": 0}

    def store(self, item: OfficeEquipment):
        if self.current_size + 1 <= self.total_size:
            current_value = self.stored_equipment.get(item.equipment_type) + 1
            self.stored_equipment[item.equipment_type] = current_value
            self.current_size += 1
        else:
            print("Склад переполнен")

    def consume(self, equipment_type: str, consuming_amount: int):
        equipment_amount = self.stored_equipment.get(equipment_type)
        if equipment_amount - consuming_amount >= 0:
            self.current_size -= consuming_amount
            changed_amount = self.stored_equipment[equipment_type] - amount
            self.stored_equipment[equipment_type] = changed_amount
        else:
            print(f"На складе нет достаточно оборудования с типом {equipment_type}")


warehouse = Warehouse(100)
eq_type = input("Введите тип офисного оборудования (Printer, Scanner или Copier): ")
amount = int(input("Введите количество данного оборудования:"))
if eq_type != "Printer" and eq_type != "Scanner" and eq_type != "Copier":
    print("Вы ввели несуществующих тип оборудования. Программа прощается с Вами")
    exit(1)
else:
    if eq_type == "Printer":
        for i in range(amount):
            warehouse.store(Printer(True, 10))
    elif eq_type == "Scanner":
        for i in range(amount):
            warehouse.store(Scanner(True, 15))
    else:
        for i in range(amount):
            warehouse.store(Copier(True, 20))

print(f"Текущая заполненность склада {warehouse.current_size} из {warehouse.total_size}")
consume_amount = int(input("Сколько хотите забрать техники со склада?" ))
warehouse.consume(eq_type, consume_amount)
print(f"Текущая заполненность склада {warehouse.current_size} из {warehouse.total_size}")
