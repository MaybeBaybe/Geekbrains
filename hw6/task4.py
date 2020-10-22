"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""
"""
Чтобы работать с унаследованными атрибутами, нужно их перечислить, например, super().__init__(color, param_1, param_2).
Тем самым мы показываем, что хотим иметь возможность работы с атрибутами класса-родителя. 
Если атрибуты не перечислить, то при попытке обращения к ним через экземпляр класса-наследника возникнет ошибка.
"""


class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Car went"

    def stop(self):
        return f"Car stopped"

    def turn(self, direction):
        return f"Car turned to {direction}"

    def show_speed(self):
        return f"Speed is {self.speed}"


class TownCar(Car):
    """
    :param speed < 60
    """

    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return self.speed if self.speed < 60 else f"Speed of auto is bigger than 60 km/hour"


class SportCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    """
    :param speed < 40
    """

    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return self.speed if self.speed < 40 else f"Speed of auto is bigger than 40 km/hour"


class PoliceCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


my_town_car = TownCar(69.5, "Green", "Bentley", is_police=False)
my_work_car = WorkCar(37.8, "White", "VAZ", False)
print(my_town_car.show_speed())
print(my_work_car.show_speed())
