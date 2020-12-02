class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        dict = ''
        for row in self.list:
            for el in row:
                dict += f'{el}\t'
            dict += '\n'
        return dict

    def __add__(self, other):
        dict = []
        for i in range(len(self.list)):
            temp = []
            for a in range(len(self.list[i])):
                temp.append(self.list[i][a] + other.list[i][a])
            dict.append(temp)
        return Matrix(dict)


matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix([[1, 2, 3], [4, 5, 6]])

print(matrix1 + matrix2)