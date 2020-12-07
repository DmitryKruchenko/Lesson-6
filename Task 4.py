"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
 (булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
  повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в
  базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar
  и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
  выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
# класс Transport
class Car:
    def __init__(self,  color, name, speed, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print("Автомобиль", self.name, 'цвета:', self.color, "начал движение")

    def stop(self):
        print("Автомобиль", self.name, "цвета:", self.color, "остановился")

    def turn(self):
        right = bool
        left = bool
        if right == True:
            print("Автомобиль", self.name, "цвета:", self.color, "повернул направо")
        else:
            print("Автомобиль", self.name, "цвета:", self.color, "повернул налево")

    def show_speed(self):
        print("Скорость автомобиля:", self.name, "цвета:", self.color, self.speed)

# классы, наследующие Car
class TownCar(Car):
    def __init__(self, color, name, speed, is_police):
        super().__init__(color, name, speed, is_police)
    def show_speed(self):
        if self.speed > 60:
            print("Автомобиль", self.name, "цвета:", self.color, "движется с первышением скорости")

    pass

class SportCar(Car):
    def __init__(self, color, name, speed, is_police):
        super().__init__(color, name, speed, is_police)
    pass

class WorkCar(Car):
    def __init__(self, color, name, speed, is_police):
        super().__init__(color, name, speed, is_police)
    def show_speed(self):
        if self.speed > 40:
            print("Автомобиль", self.name, "цвета:", self.color, "движется с первышением скорости")
    pass

class PoliceCar(Car):
    def __init__(self, color, name, speed, is_police):
        super().__init__(color, name, speed, is_police)
    pass

a = Car('black', 'Ferrari', 80, False)
print(a.go())
b = PoliceCar('white', 'Ford', 90, True)
print(type(b))

print(b.show_speed())

c = TownCar('yellow', 'Porter', 100, False)
print(c.show_speed())




