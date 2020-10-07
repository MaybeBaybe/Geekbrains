"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def user(first_name, last_name, year_of_birth, city_of_residence, email, phone):
    return f"User data: {first_name}, {last_name}, {year_of_birth}, {city_of_residence}, {email}, {phone}"


print(
    user(
        first_name="Jhon",
        last_name="Butcher",
        year_of_birth="1978",
        city_of_residence="Kanada",
        email="butcher",
        phone="+33382342314")
)
