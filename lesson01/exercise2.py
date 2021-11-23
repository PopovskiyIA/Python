input_seconds = int(input("Введите время в секундах: "))

hours = input_seconds // 3600
minutes = input_seconds % 3600 // 60
seconds = input_seconds % 3600 % 60

print(f"Время в формате чч:мм:cc - {hours:d}:{minutes:02d}:{seconds:02d}")
