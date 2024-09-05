from utils import get_number


# 1) Проверка числа
def check_number_value():
    try:
        number = get_number("Введите число: ")
        if number > 10:
            print("Число больше десяти")
        elif number < 10:
            print("Число меньше десяти")
        else:
            print("Число равно десяти")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число.")


# 2) Сравнение двух
def compare_numbers(first_number, second_number):
    if first_number > second_number:
        return "Первое число больше второго."
    elif first_number < second_number:
        return "Первое число меньше второго."
    else:
        return "Первое число равно второму."


def two_num_compare():
    while True:
        try:
            first_number = get_number("Введите первое число: ")
            second_number = get_number("Введите второе число: ")
            result = compare_numbers(first_number, second_number)
            print(result)

            continue_choice = input("Хотите сравнить еще два числа? (да/нет): ").strip().lower()
            if continue_choice != 'да':
                print("Спасибо за использование программы!")
                break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")


# 3) Тип треугольника
def get_side_length(prompt):
    while True:
        try:
            length = float(input(prompt))
            if length <= 0:
                raise ValueError("Длина стороны должна быть положительным числом.")
            return length
        except ValueError as e:
            print(f"Ошибка: {e}")


def determine_triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        return "Треугольник равносторонний."
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Треугольник равнобедренный."
    else:
        return "Треугольник разносторонний."


def triangle():
    print("Введите длины сторон треугольника:")
    side1 = get_side_length("Длина первой стороны: ")
    side2 = get_side_length("Длина второй стороны: ")
    side3 = get_side_length("Длина третьей стороны: ")

    triangle_type = determine_triangle_type(side1, side2, side3)
    print(triangle_type)


# 4) Четыре числа
def four_numbers():
    positive_count = 0
    negative_count = 0

    print("Введите четыре числа (можно использовать дробные):")
    for i in range(4):
        number = get_number(f"Число {i + 1}: ")

        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1

    print(f"Количество положительных чисел: {positive_count}")
    print(f"Количество отрицательных чисел: {negative_count}")


# 5) Три числа
def main_numbers():
    print("Введите три числа:")
    numbers = []
    for i in range(3):
        number = get_number(f"Число {i + 1}: ")
        numbers.append(number)

    max_number = max(numbers)
    print(f"Самое большое число: {max_number}")

# 6)
def sum_of_three():
    print("Введите три числа:")
    numbers = []

    for i in range(3):
        number = get_number(f"Число {i + 1}: ")
        numbers.append(number)  # Добавляем введенное число в список

    max_number = max(numbers)  # Находим максимальное число
    min_number = min(numbers)  # Находим минимальное число
    sum_of_extremes = max_number + min_number  # Считаем сумму

    print(f"Сумма наибольшего ({max_number}) и наименьшего ({min_number}) чисел равна: {sum_of_extremes}")

# 7) Чётное или нет
def is_even(number):
    """Проверяет, является ли число четным."""
    return number % 2 == 0

def check_numbers_odd():
    """Запрашивает у пользователя числа и выводит, четные они или нечетные."""
    while True:
        user_input = input("Введите число (или 'exit' для выхода): ")

        if user_input.lower() == 'exit':
            print("Выход из программы.")
            break  # Завершаем программу

        try:
            number = int(user_input)  # Преобразуем ввод в целое число
            if is_even(number):
                print(f"{number} является четным числом.")
            else:
                print(f"{number} является нечетным числом.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")


# 8) Магазин
def display_menu(products):
    """Отображает меню товаров."""
    print("Доступные товары:")
    for i, (product, price) in enumerate(products.items(), start=1):
        print(f"{i}. {product} - {price} рублей")


def shop():
    products = {
        "Яйца": 50,
        "Жвачка": 30,
        "Юмбики": 65
    }

    display_menu(products)

    while True:
        try:
            choice = int(input("Выберите номер товара (1-3) или 0 для выхода: "))
            if choice == 0:
                print("Выход из программы.")
                break

            if choice < 1 or choice > len(products):
                print("Некорректный выбор. Пожалуйста, выберите номер товара от 1 до 3.")
                continue

            product_name = list(products.keys())[choice - 1]
            product_price = products[product_name]

            money = get_number(f"Введите сумму денег для покупки '{product_name}' (цена: {product_price} рублей): ")

            if money < product_price:
                print("Денег не хватает!")
            elif money == product_price:
                print("Спасибо за покупку!")
            else:
                change = money - product_price
                print(f"Ваша сдача: {change:.2f} рублей")

        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число для выбора товара и корректное число для суммы.")