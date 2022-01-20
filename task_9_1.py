#1. Создать класс TrafficLight (светофор).

import time

class Trafficlight:
    __color = [('красный', 7), ('желтый', 2), ('зеленый', 4)]

    def running(self):
        for c, t in self.__color:
            print(f'{c} включен на {t} сек.')
            time.sleep(t)


a = Trafficlight()
Trafficlight.running(a)

