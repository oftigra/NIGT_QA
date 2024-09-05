import random
from collections import Counter

def pos_neg(numbers):
    count_positive = 0
    count_negative = 0

    for num in numbers:
        if num > 0:
            count_positive += 1
        elif num < 0:
            count_negative += 1

    return count_positive, count_negative


def pos_neg_numb():
    # Генерируем массив с 10 случайными целыми числами в диапазоне от -20 до 20
    size = 10  # Размер массива
    numbers = [random.randint(-5, 5) for _ in range(size)]

    print(f"Сгенерированный массив: {numbers}")

    positive_count, negative_count = pos_neg(numbers)

    print(f"Количество положительных чисел: {positive_count}")
    print(f"Количество отрицательных чисел: {negative_count}")


# 2)Сумма элементов четных индекс
def sum_of_index():
    size = 10  # Размер массива
    numbers = [random.randint(-10, 10) for _ in range(size)]
    print(f"Сгенерированный массив: {numbers}")

    index_elem = list(map(lambda i: numbers[i], range(0, len(numbers), 2)))

    index_sum = sum(index_elem)

    print(f"Сумма элементов с четными индексами: {index_sum}")


# 3) Четные элементы и индексы
def divide(num):
    return num % 2 == 0


def pos_elem_2():
    size = 10  # Размер массива
    numbers = [random.randint(-50, 50) for _ in range(size)]

    print(f"Сгенерированный массив: {numbers}")

    even_sum = sum(filter(divide, numbers))

    print(f"Сумма четных элементов: {even_sum}")


# 4)
def max_value():
    size = 10
    numbers = [random.randint(-10, 10) for _ in range(size)]
    print(f"Сгенерированный массив: {numbers}")

    max_number = max(numbers)
    print(f"Наибольшее число в массиве: {max_number}")


# 5)Часто встречающееся
def often_value():
    size = 30
    numbers = [random.randint(1, 10) for _ in range(size)]
    print(f"Сгенерированный массив: {numbers}")

    counter = Counter(numbers)
    max_count = max(counter.values())

    most_common_numbers = [num for num, count in counter.items() if count == max_count]

    if max_count > 1:
        result = max(most_common_numbers)
        print(f"Наиболее часто встречающееся число: {result}")
    else:
        print("Нет повторяющихся чисел.")



#6) 9_9
def from9_to_9():
    size = 10
    array = [[random.randint(1, 100) for _ in range(size)] for _ in range(size)]

    print("Сгенерированный двумерный массив:")
    for row in array:
        print(row)

    print("\nЧисла по диагонали (от [0][0] до [9][9]):")
    for i in range(size):
        print(array[i][i])


#7) 0_10
def from0_to_10():
    size = 10
    array = [[random.randint(1, 100) for _ in range(size)] for _ in range(size)]

    print("Сгенерированный двумерный массив:")
    for row in array:
        print(row)

    print("\nЧисла по диагонали (от [0][9] до [9][0]):")
    for i in range(size):
        print(array[i][size - 1 - i])



# 8) Сумма столбца
def sum5_5():
    size = 5
    array = [[random.randint(1, 100) for _ in range(size)] for _ in range(size)]

    print("Сгенерированный двумерный массив:")
    for row in array:
        print(row)

    column_sums = [0] * size

    for j in range(size):
        for i in range(size):
            column_sums[j] += array[i][j]

    print("\nСуммы чисел в каждом столбце:")
    for j in range(size):
        print(f"Сумма столбца {j}: {column_sums[j]}")

    max_sum = max(column_sums)
    print(f"\nНаибольшая сумма столбца: {max_sum}")

