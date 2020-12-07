"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
 зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
 третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
 порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""
from itertools import cycle
import time

class TrafficLight:
    # атрибуты класса
    _color = ['red', 'yellow', 'green']
    time_color = [7, 3, 5]

    # методы класса
    def running(self):
        iter_color = cycle(TrafficLight._color)
        iter_time_color = cycle(TrafficLight.time_color)
        i = True
        while i == True:
            print(next(iter_color))
            time.sleep(next(iter_time_color))





trafficLight = TrafficLight()
print(trafficLight)
trafficLight.running()

