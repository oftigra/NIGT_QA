from ternary_operator import (
    check_number_value,
    two_num_compare,
    triangle,
    four_numbers,
    main_numbers,
    sum_of_three,
    check_numbers_odd,
    shop,
)

if __name__ == "__main__":
    while True:
        print("\nВыберите задачу для выполнения:")
        print("1. Проверка числа")
        print("2. Сравнение двух чисел")
        print("3. Определение типа треугольника")
        print("4. Подсчет положительных и отрицательных чисел")
        print("5. Найти максимальное число среди трех")
        print("6. Найти сумму трёх")
        print("7. Чётное или нет")
        print("8. Магазин")
        print("0. Выход")

        choice = input("Ваш выбор (введите номер задачи): ")

        if choice == '1':
            check_number_value()
        elif choice == '2':
            two_num_compare()
        elif choice == '3':
            triangle()
        elif choice == '4':
            four_numbers()
        elif choice == '5':
            main_numbers()
        elif choice == '6':
            sum_of_three()
        elif choice == '7':
            check_numbers_odd()
        elif choice == '8':
            shop()
        elif choice == '0':
            print("Спасибо за использование программы!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите номер задачи.")