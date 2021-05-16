from abc import ABC, abstractmethod


class NewAbstractClass(ABC):
    @abstractmethod
    def show_fabric_size(self):
        pass


class Costume(NewAbstractClass):
    def __init__(self, costume_parameter):
        self.H = costume_parameter
        self.costume_size = 2 * self.H + 0.3

    @property
    def show_fabric_size(self):
        return f"Расход ткани на костюм составляет {self.costume_size}"


class Coat(NewAbstractClass):
    def __init__(self, coat_parameter):
        self.V = coat_parameter
        self.coat_size = self.V / 6.5 + 0.5

    @property
    def show_fabric_size(self):
        return f"Расход ткани на пальто составляет {self.coat_size}"


class Clothes:
    def __init__(self):
        self.coat_pieces = []
        self.costume_pieces = []

    def add_coat(self, coat_parameter):
        self.coat_pieces.append(Coat(coat_parameter))

    def add_costume(self, costume_parameter):
        self.costume_pieces.append(Costume(costume_parameter))

    @property
    def common_fabric_size(self):
        total_fabric_size = 0
        for el in self.coat_pieces:
            total_fabric_size += el.coat_size
        for el in self.costume_pieces:
            total_fabric_size += el.costume_size
        return f"Суммарный расход ткани на производство одежды составляет {total_fabric_size}"


coat_1 = Coat(20)
coat_2 = Coat(25)
costume_1 = Costume(1.65)
costume_2 = Costume(1.80)
print(coat_1.show_fabric_size)
print(coat_2.show_fabric_size)
print(costume_1.show_fabric_size)
print(costume_2.show_fabric_size)
pieces_of_clothes = Clothes()
pieces_of_clothes.add_coat(20)
pieces_of_clothes.add_coat(25)
pieces_of_clothes.add_costume(1.80)
pieces_of_clothes.add_costume(1.65)
print(pieces_of_clothes.common_fabric_size)
