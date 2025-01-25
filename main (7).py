import numpy as np

def process_matrix():
    def inner_process(file_name):
        # Чтение матрицы из текстового файла
        with open(file_name, 'r') as file:
            matrix = np.loadtxt(file, dtype=float)
        
        # Задача 1: Найти максимальный среди минимальных элементов строк
        min_elements = np.min(matrix, axis=1)
        max_of_mins = np.max(min_elements)
        
        # Задача 2: Отсортировать матрицу по столбцам по возрастанию
        sorted_matrix = np.sort(matrix, axis=0)
        
        return max_of_mins, sorted_matrix

    # Имя файла с матрицей
    file_name = input("Введите имя файла с матрицей: ").strip()
    max_of_mins, sorted_matrix = inner_process(file_name)

    # Вывод результатов
    print(f"Максимальный среди минимальных элементов строк: {max_of_mins}")
    print("Матрица, отсортированная по столбцам по возрастанию:")
    print(sorted_matrix)

# Вызов основной функции
process_matrix()
