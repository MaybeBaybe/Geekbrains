"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name: str
    surname: str
    position: str
    wage: float
    bonus: float
    _income: dict

    def __init__(self, name, surname, position, wage: float = 0, bonus: float = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"The full name of employee is {self.name} {self.surname}"

    def get_total_income(self):
        return f"The salary of employee is {(self.wage + self.bonus)} without tax"


check_pos = Position("John", "Parkees", "marketing manager", 12.500, 2000)
print(check_pos.get_full_name())
print(check_pos.get_total_income())
