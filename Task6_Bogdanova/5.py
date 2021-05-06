class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        pass

    def draw(self):
        print("Запуск отрисовки ручкой.")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        pass

    def draw(self):
        print("Запуск отрисовки карандашом.")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        pass

    def draw(self):
        print("Запуск отрисовки маркером.")


a = Stationery("Последний рисунок")
print(a.title)
a.draw()
b = Pen("Последний рисунок")
print(b.title)
b.draw()
c = Pencil("Последний рисунок")
print(c.title)
c.draw()
d = Handle("Последний рисунок")
print(d.title)
d.draw()
