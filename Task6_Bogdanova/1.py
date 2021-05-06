import time
from itertools import cycle


class TrafficLight:
    __color = ["красный", "жёлтый", "зелёный"]

    def running(self):
        inspector = "зелёный"
        a = 0
        for i in cycle(TrafficLight.__color):
            if a <= 10:
                if i == "красный":
                    if inspector == "зелёный":
                        print(i)
                        time.sleep(7)
                        inspector = "красный"
                        a += 1
                    else:
                        print("Ошибка в работе светофора")
                        break
                elif i == "жёлтый":
                    if inspector == "красный":
                        print(i)
                        time.sleep(2)
                        inspector = "жёлтый"
                        a += 1
                    else:
                        print("Ошибка в работе светофора")
                        break
                else:
                    if inspector == "жёлтый":
                        print(i)
                        time.sleep(10)
                        inspector = "зелёный"
                        a += 1
                    else:
                        print("Ошибка в работе светофора")
                        break
            else:
                break


b = TrafficLight()
b.running()
