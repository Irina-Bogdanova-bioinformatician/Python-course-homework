class Car:
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        return "Машина поехала!"

    def stop(self):
        return "Машина остановилась!"

    def turn(self):
        return f"Машина повернула {self.direction}."

    def show_speed(self):
        return f"Текущая скорость автомобиля равна {self.speed} км/ч."


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)
        pass

    def show_speed(self):
        if self.speed > 60:
            return f"Текущая скорость автомобиля равна {self.speed} км/ч. Скорость превышена!"
        else:
            return f"Текущая скорость автомобиля равна {self.speed} км/ч."


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)
        pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)
        pass

    def show_speed(self):
        if self.speed > 40:
            return f"Текущая скорость автомобиля равна {self.speed} км/ч. Скорость превышена!"
        else:
            return f"Текущая скорость автомобиля равна {self.speed} км/ч."


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)
        pass


a = Car(70, "blue", "Audi", False, "направо")
print(a.go(), a.stop(), a.turn(), a.show_speed())
print(a.speed, a.color, a.name, a.is_police, a.direction)

b = TownCar(80, "white", "Renault", False, "налево")
print(b.go(), b.stop(), b.turn(), b.show_speed())
print(b.speed, b.color, b.name, b.is_police, b.direction)

c = WorkCar(45, "red", "Ford Focus", False, "направо")
print(c.go(), c.stop(), c.turn(), c.show_speed())
print(c.speed, c.color, c.name, c.is_police, c.direction)

d = PoliceCar(100, "black", "Jeep", True, "налево")
print(d.go(), d.stop(), d.turn(), d.show_speed())
print(d.speed, d.color, d.name, d.is_police, d.direction)

e = SportCar(200, "green", "Maserati", False, "направо")
print(e.go(), e.stop(), e.turn(), e.show_speed())
print(e.speed, e.color, e.name, e.is_police, e.direction)
