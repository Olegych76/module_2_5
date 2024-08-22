def get_matrix(n, m, value):
    matrix = []  # объявляем переменную
    for i in range(n):  # добавляем очередную (пустую) строку в список:
        matrix.append([])
        for j in range(m):  # заполняем эту строку списка значением value:
            matrix[i].append(value)
    return matrix  # возвращаем заполненную матрицу


print(get_matrix(2, 2, 10))  # две строки, два столбца
print(get_matrix(2, 5, 7))  # две строки, пять столбцов
print(get_matrix(6, 2, 5))  # шесть строк, два столбца
