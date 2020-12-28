#1

# class Matrix:
#     def __init__(self, list_1, list_2):
#         self.list_1 = list_1
#         self.list_2 = list_2
#
#     def __add__(self):
#         matrix = [[0, 0, 0],
#                 [0, 0, 0],
#                 [0, 0, 0]]
#
#         for i in range(len(self.list_1)):
#
#             for j in range(len(self.list_2[i])):
#                 matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]
#
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))
#
#     def __str__(self):
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))
#
# my_matrix = Matrix([[3, 15, 10],
#                     [5, 12, 24],
#                     [39, 62, 21]],
#                    [[54, 7, 5],
#                     [13, 9, 73],
#                     [11, 8, 16]])
#
# print(my_matrix.__add__())


#2

# class Textil:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square_c(self):
#         return self.width / 6.5 + 0.5
#
#     def get_square_j(self):
#         return self.height * 2 + 0.3
#
#     @property
#     def get_sq_full(self):
#         return str(f'Общая ткань \n'
#                    f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')
#
# class Coat(Textil):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#         self.square_c = round(self.width / 6.5 + 0.5)
#
#     def __str__(self):
#         return f'Пальто {self.square_c}'
#
# class Jacket(Textil):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#         self.square_j = round(self.height * 2 + 0.3)
#
#     def __str__(self):
#         return f'Костюм {self.square_j}'
#
# coat = Coat(2, 4)
# jacket = Jacket(1, 2)
# print(coat)
# print(jacket)
# print(coat.get_sq_full)
# print(jacket.get_sq_full)
# print(jacket.get_square_c())
# print(jacket.get_square_j())


#3

# class Cell:
#     def __init__(self, quantity):
#         self.quantity = int(quantity)
#
#     def __str__(self):
#         return f'Результат {self.quantity * "*"}'
#
#     def __add__(self, other):
#         return Cell(self.quantity + other.quantity)
#
#     def __sub__(self, other):
#         return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно')
#
#     def __mul__(self, other):
#         return Cell(int(self.quantity * other.quantity))
#
#     def __truediv__(self, other):
#         return Cell(round(self.quantity // other.quantity))
#
#     def make_order(self, cells_in_row):
#         row = ''
#         for i in range(int(self.quantity / cells_in_row)):
#             row += f'{"*" * cells_in_row} \\n'
#         row += f'{"*" * (self.quantity % cells_in_row)}'
#         return row
#
# cells1 = Cell(33)
# cells2 = Cell(9)
# print(cells1)
# print(cells1 + cells2)
# print(cells2 - cells1)
# print(cells2.make_order(5))
# print(cells1.make_order(10))
# print(cells1 / cells2)

