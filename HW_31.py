# Напишите функцию для транспонирования матрицы

def transpose(matrix):
    # Проверяем, не пустая ли матрица
    if not matrix or not matrix[0]:
        return []
    
    # Создаем новую матрицу с нужными размерами
    transposed = [[0] * len(matrix) for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]

    return transposed

# для проверки
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = transpose(matrix)
print(result)

