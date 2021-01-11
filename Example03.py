"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()),
умножение (mul()), деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""
# Определение класса Cell
class Cell:
    # Перегрузка конструктора класса Cell
    def __init__(self, quantity):
        self.quantity = quantity
    # Перегрузка метода add() для реализации объединения двух клеток
    def __add__(self, other):
        return other.quantity + self.quantity

    # Перегрузка метода sub() для реализации разности количества ячеек двух клеток
    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return self.quantity - other.quantity
        else:
            print("Разность количества клеток меньше нуля")

    # Перегрузка метода mul() для создания общей клетки из двух.
    # Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток
    def __mul__(self, other):
        return other.quantity * self.quantity
    # Перегрузка метода truediv() для создания общей клетки из двух.
    # Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
    def __truediv__(self, other):
        return self.quantity // other.quantity
    # Метод организации ячеек клетки по рядам
    def make_order(self, cell_in_row):
        i = 0
        new_row = ""
        while i < self.quantity // cell_in_row:
            new_row = new_row + "*" * cell_in_row + '\n'
            i = i + 1
        new_row = new_row + "*" * (self.quantity % cell_in_row) + '\n'
        return new_row

cell_a = Cell(30)
print(cell_a.make_order(6))
cell_b = Cell(25)
print(cell_b.make_order(5))
print(cell_a.__add__(cell_b))
print(cell_a.__sub__(cell_b))
print(cell_a.__mul__(cell_b))
print(cell_a.__truediv__(cell_b))