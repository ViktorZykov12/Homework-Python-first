class Cell:
    def __init__(self, num):
        self.num = int(num)

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        result = self.num - other.num
        return f'{result}' if result > 0 else 'Вычитание невозможно'

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num // other.num

    def make_order(self, row):
        box_row = int(self.num / row)
        box = ''
        for i in range(box_row):
            box += '*' * row + '\n'
        box += (self.num - box_row * row) * '*'
        return box


cell_1 = Cell(55)
cell_2 = Cell(25)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(10))