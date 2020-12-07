"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""
class Worker:
    # атрибуты класса
    def __init__(self, worker_code, name, surname, position, income):
        self.worker_code = worker_code
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    # методы класса
    def __init__(self, worker_code, name, surname, position, _income):
        super().__init__(worker_code, name, surname, position, _income)

    def get_full_name(self):
        return f"Полное имя: {self.name}, {self.surname}"

    def get_total_income(self):
        return f"Полный доход: {self._income}"




worker_cod = 1
name = 'Dmitry'
surname = 'Kruchenko'
position = 'CEO'
income = {'wage': 3000, 'bonus': 2000}

worker_1 = Position(1, 'Dmitry', 'Kruchenko', 'CEO', income)
print(worker_1.get_full_name())
print(worker_1.get_total_income())