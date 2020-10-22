"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и
проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        """
        :return: Метод выводит сообщение “Запуск отрисовки.”
        """
        return "Start rendering"


class Pen(Stationery):
    def __init__(self, title):
        super(Pen, self).__init__(title)

    def draw(self):
        return "Start rendering with a pen"


class Pencil(Stationery):
    def __init__(self, title):
        super(Pencil, self).__init__(title)

    def draw(self):
        return "Start rendering with a pencil"


class Handle(Stationery):
    def __init__(self, title):
        super(Handle, self).__init__(title)

    def draw(self):
        return "Start rendering with a handle"


my_pen = Pen("Littler")
my_pencil = Pencil("Garota")
my_handle = Handle("Black shown")

print(my_pen.draw())
print(my_pencil.draw())
print(my_handle.draw())
