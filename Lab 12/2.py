class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def display(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))

    def __add__(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                element = 0
                for k in range(3):
                    element += self.matrix[i][k] * other.matrix[k][j]
                row.append(element)
            result.append(row)
        return Matrix(result)

    def transpose(self):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.matrix[j][i])
            result.append(row)
        return Matrix(result)


A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matrix A:")
A.display()

print("\nMatrix B:")
B.display()

C = A + B
print("\nA + B:")
C.display()

D = A * B
print("\nA * B:")
D.display()

print("\nTranspose of A:")
A_T = A.transpose()
A_T.display()

print("\nTranspose of B:")
B_T = B.transpose()
B_T.display()
