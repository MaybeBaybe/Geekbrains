"""
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны передаваться
при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road():
    _length: float
    _width: float

    def __init__(self, length=0, width=0):
        self._length = length
        self._width = width

    def calc(self):
        mass_of_asphalt = float(input("Enter the mass in kg: "))
        asph_thickness = float(input("Enter the thickness in sm: "))
        return print(f"{self._length} * {self._width} * {mass_of_asphalt} * {asph_thickness} / 1000 for tons: " +
                     str(self._length * self._width * mass_of_asphalt * asph_thickness / 1000))


my_road = Road(20, 5000)
my_road.calc()
