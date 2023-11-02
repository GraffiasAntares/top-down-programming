import random


# Алгоритм задания
def algorythm(row, matrix):
    for i in range(row):
        matrix[i].append(sum(map(abs, matrix[i])))
    matrix.sort(key=last_value, reverse=True)
    return matrix


# функция для key в sort()
def last_value(matrix):
    pass


# Ввод матрицы вручную
def matrix_input(row, column):
    matrix = [[0 for j in range(column)] for i in range(row)]
    for i in range(row):
        for j in range(column):
            while True:
                print(f"[{i}][{j}]:", end="")
                try:
                    matrix[i][j] = int(input())
                    break
                except ValueError:
                    print("\nВводите только целые значения!\n")
    return matrix


# Генерирование матрицы
def matrix_generation(row, column):
    matrix = [[random.randint(-100, 100) for j in range(column)] for i in range(row)]
    return matrix


# Ввод размерности матрицы
def input_matrix_dem():
    pass


# Вывод матрицы
def show_matrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end='    ')
        print()


# Функция корректного присваивания типа int
def int_input(inpt):
    pass


def main():
    matrix = None
    while True:
        print("\n"
              "[1] Ввод матрицы вручную\n"
              "[2] Генерирование матрицы\n"
              "[3] Запуск алгоритма\n"
              "[4] Вывод результата\n"
              "[5] Завершение программы\n"
              )
        menu_input = int_input(input("..."))

        match menu_input:
            # [1] Ручной ввод
            case 1:
                print("\nВведите размерность матрицы через пробел: строки столбцы\n")
                row, column = input_matrix_dem()
                matrix = matrix_input(row, column)
                print("\nВыполнено успешно\n")
                input("Нажмите Enter для продолжения...")

            # [2] Генерирование матрицы
            case 2:
                print("\nВведите размерность матрицы через пробел: строки столбцы\n")
                row, column = input_matrix_dem()
                matrix = matrix_generation(row, column)
                print("\nВыполнено успешно\n")
                input("Нажмите Enter для продолжения...")

            # Реализация алгоритма
            case 3:
                if matrix == None:
                    print("\n"
                          "Для начала введите данные!"
                          "\n")
                    continue

                elif row != len(matrix[0]):
                    print("\nВыполнено успешно\n")
                    continue

                matrix = algorythm(row, matrix)
                print("\nВыполнено успешно\n")

            # Вывод результата
            case 4:
                if (matrix != None) and (row != len(matrix[0])):
                    print("\nВаша матрица:")
                    show_matrix(matrix, row, column + 1)
                    input("Нажмите Enter для продолжения...")

                else:
                    print("\n"
                          "Сначала введите данные и выполните алгоритм!"
                          "\n")
                    continue
            case 5:
                exit()
            case _:
                print("\nОшибка ввода\n")


if __name__ == "__main__":
    main()
