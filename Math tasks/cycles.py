import math


# 1) Умножение на 4
def multi():
    print("Таблица умножения на 4:")
    for i in range(1, 11):
        result = 4 * i
        print(f"4 x {i} = {result}")


# 2) От ноля до х
def from_0_to_x():
    try:
        x = int(input("Введите число x: "))
        if x < 0:
            print("Ошибка: Число должно быть неотрицательным.")
        else:
            print("Четные числа от 0 до", x, ":")
            for i in range(0, x + 1, 2):
                print(i)
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")


# 3)Фиба
def preconditions(n):
    if n < 0:
        return "Ошибка: индекс не может быть отрицательным."
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fiba():
    try:
        x = int(input("Введите индекс x: "))
        result = preconditions(x)
        print(f"Число Фибоначчи с индексом {x}: {result}")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")


# 4) Факториал
def factorial():
    try:
        num = int(input("Введите число для вычисления его факториала: "))  #
        if num < 0:
            print("Ошибка: факториал не определен для отрицательных чисел.")
        else:
            factorial_result = math.factorial(num)
            print(f"Факториал числа {num} равен {factorial_result}.")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")

# 5) Символ
def symbol():
    user_input = input("Введите строку: ")

    print("Выводим строку посимвольно:")
    for character in user_input:
        print(character)
