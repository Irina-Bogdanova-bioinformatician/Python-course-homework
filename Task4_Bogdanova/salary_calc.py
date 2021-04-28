from sys import argv

script_name, hours, amount_per_hour, bonus = argv
hours, amount_per_hour, bonus = float(hours), float(amount_per_hour), float(bonus)
print("Заработная плата сотрудника составляет ", hours * amount_per_hour + bonus)
input('\nPress ENTER to exit')
