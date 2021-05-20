class Store:
    def __init__(self):
        print("Вы просматриваете данные склада.")
        self.equipment_dict = {}
        self.list_printers = []
        self.list_scanners = []
        self.list_copiers = []
        self.printers_number = 0
        self.scanners_number = 0
        self.copiers_number = 0

    def add_printer(self, model, release_year, color, price, printing_technology, colors_number):
        number = 0
        try:
            number = int(input("Ведите количество принтеров данной модели, отправляемое на склад: "))
            if number == 0:
                print("Число единиц должно превышать 0.")
        except ValueError:
            print("Вы ввели не число.")
        while number > 0:
            self.list_printers.append(Printer(model, release_year, color, price, printing_technology, colors_number))
            self.printers_number += 1
            number -= 1

    def add_scanner(self, model, release_year, color, price, scanner_type, resolution):
        number = 0
        try:
            number = int(input("Ведите количество сканеров данной модели, отправляемое на склад: "))
            if number == 0:
                print("Число единиц должно превышать 0.")
        except ValueError:
            print("Вы ввели не число.")
        while number > 0:
            self.list_scanners.append(Scanner(model, release_year, color, price, scanner_type, resolution))
            self.scanners_number += 1
            number -= 1

    def add_copier(self, model, release_year, color, price, copies_per_minute, size):
        number = 0
        try:
            number = int(input("Ведите количество копировальных машин данной модели, отправляемое на склад: "))
            if number == 0:
                print("Число единиц должно превышать 0.")
        except ValueError:
            print("Вы ввели не число.")
        while number > 0:
            self.list_copiers.append(Copier(model, release_year, color, price, copies_per_minute, size))
            self.copiers_number += 1
            number -= 1

    @property
    def get_equipment_number(self):
        self.equipment_dict["printers"] = self.printers_number
        self.equipment_dict["scanners"] = self.scanners_number
        self.equipment_dict["copiers"] = self.copiers_number
        return f'Количество оргтехники на складе: {self.equipment_dict}'

    @property
    def get_all_printers(self):
        final_list = []
        for el in self.list_printers:
            final_list.append(el.printer_dict)
        return f'Принтеры, представленные на складе: {final_list}'

    @property
    def get_all_scanners(self):
        final_list = []
        for el in self.list_scanners:
            final_list.append(el.scanner_dict)
        return f'Сканеры, представленные на складе: {final_list}'

    @property
    def get_all_copiers(self):
        final_list = []
        for el in self.list_copiers:
            final_list.append(el.copier_dict)
        return f'Копировальные машины, представленные на складе: {final_list}'


class OfficeEquipment:
    def __init__(self, model, release_year, color, price):
        self.model = model
        self.release = release_year
        self.color = color
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, model, release_year, color, price, printing_technology, colors_number):
        super().__init__(model, release_year, color, price)
        self.printing_tech = printing_technology
        self.colors_number = colors_number
        self.printer_dict = {"model": self.model, "release year": self.release, "color": self.color,
                             "price": self.price, "printing_technology": self.printing_tech,
                             "number of colors": self.colors_number}


class Scanner(OfficeEquipment):
    def __init__(self, model, release_year, color, price, scanner_type, resolution):
        super().__init__(model, release_year, color, price)
        self.scanner_type = scanner_type
        self.resolution = resolution
        self.scanner_dict = {"model": self.model, "release year": self.release, "color": self.color,
                             "price": self.price, "scanner type": self.scanner_type,
                             "resolution": self.resolution}


class Copier(OfficeEquipment):
    def __init__(self, model, release_year, color, price, copies_per_minute, size):
        super().__init__(model, release_year, color, price)
        self.copies_per_minute = copies_per_minute
        self.size = size
        self.copier_dict = {"model": self.model, "release year": self.release, "color": self.color,
                            "price": self.price, "copies per minute": self.copies_per_minute,
                            "size": self.copies_per_minute}


equipment = Store()
equipment.add_copier("A234", 2020, "black", 3500, 12, "portable")
equipment.add_copier("A235", 2019, "silver", 3400, 13, "portable")
equipment.add_printer("B-579f", 2021, "black", 4500, "ink", 8)
equipment.add_printer("C-1000", 2018, "grey", 5000, "ink", 8)
equipment.add_scanner("E4556", 2020, "black", 3900, "tablet", 600)
equipment.add_scanner("P-1080", 2019, "white", 4100, "tablet", 1200)
print(equipment.get_all_copiers)
print(equipment.get_all_printers)
print(equipment.get_all_scanners)
print(equipment.get_equipment_number)
