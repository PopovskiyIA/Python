# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

def print_user_info(name, surname, year_of_birth, city_of_residence, email, phone_number):
    """
    Функция выводит данные о пользователе в одну строку

    :param name: имя пользователя
    :param surname: фамилия пользователя
    :param year_of_birth: год рождения
    :param city_of_residence: город проживания
    :param email: адрес электронной почты
    :param phone_number: номер телефона
    """
    print(
        f"Данные пользователя: имя = {name}, фамилия = {surname}, год рождения = {year_of_birth}, "
        f"город проживания = {city_of_residence}, email = {email}, телефон = {phone_number}")


# тест
print_user_info(surname="Петров", name="Пётр", email="petrov@pochta.ru", phone_number="555-555-555",
                city_of_residence="Москва", year_of_birth=2000)
