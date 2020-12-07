"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего
дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра
дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
class Road:
    # атрибуты класса
    _lenght = float
    _width = float

    # методы класса
    def __init__(self, lenght, widht, height):
        self.lenght = lenght
        self.widht = widht
        self.height = height

    def road_calculation(self):
        asphalt_density = 2000 # kg / m3
        asphalt_mass = asphalt_density * self.lenght * self.widht * self.height / 100
        print('Масса асфальта, кг:', asphalt_mass)


lenght = float(input('Введите длину дорожного полона в м: '))
widht = float(input('Введите ширину дорожного полотна в м: '))
height = float(input('Ведите толщину дорожного полотна в см: '))

road_mass = Road(lenght, widht, height)


road_mass.road_calculation()
