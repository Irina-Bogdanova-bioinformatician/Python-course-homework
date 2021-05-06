class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def coating_mass(self):
        mass = self._length * self._width * 25 * 5
        if (mass // 1000) >= 1:
            print(f"При толщине покрытия 5 см масса асфальта, необходимого для покрытия дорожного полотна, "
                  f"равна {mass / 1000} т")
        else:
            print(f"При толщине покрытия 5 см масса асфальта, необходимого для покрытия дорожного полотна, "
                  f"равна {mass} кг")


a = Road(20, 5000)
a.coating_mass()
