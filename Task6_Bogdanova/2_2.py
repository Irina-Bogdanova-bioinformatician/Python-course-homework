class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def coating_mass(self):
        depth = float(input("Введите значение толщины покрытия в см "))
        kilo_per_m = float(input("Введите массу (в кг) 1 квадратного метра покрытия толщиной 1 см "))
        mass = self._length * self._width * kilo_per_m * depth
        if (mass // 1000) >= 1:
            print(f"При толщине покрытия {depth} см масса асфальта, необходимого для покрытия дорожного полотна, "
                  f"равна {mass / 1000} т")
        else:
            print(f"При толщине покрытия {depth} см масса асфальта, необходимого для покрытия дорожного полотна, "
                  f"равна {mass} кг")


a = Road(20, 5000)
a.coating_mass()
