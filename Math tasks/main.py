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

from cycles import (
    multi,
    from_0_to_x,
    fiba,
    factorial,
    symbol,
)

from arrays import (
    pos_neg_numb,
    sum_of_index,
    pos_elem_2,
    max_value,
    often_value,
    from9_to_9,
    from0_to_10,
    sum5_5,
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
        print("9. Таблица умножения х4")
        print("10. От 0 до Х")
        print("11. Фиба")
        print("12. Факториал")
        print("13. Символ")
        print("14. Позитив негатив")
        print("15. Сумма элементов четных индекс")
        print("16. Сумма элементов четных индекс(значения")
        print("17. Макс значение в массиве")
        print("18. Часто встречающееся")
        print("19. Массив от 9 до 9")
        print("20. Массив от 0 до 9")
        print("21. 5x5 сумма столбца")

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
        elif choice == '9':
            multi()
        elif choice == '10':
            from_0_to_x()
        elif choice == '11':
            fiba()
        elif choice == '12':
            factorial()
        elif choice == '13':
            symbol()
        elif choice == '14':
            pos_neg_numb()
        elif choice == '15':
            sum_of_index()
        elif choice == '16':
            pos_elem_2()
        elif choice == '17':
            max_value()
        elif choice == '18':
            often_value()
        elif choice == '19':
            from9_to_9()
        elif choice == '20':
            from0_to_10()
        elif choice == '21':
            sum5_5()
        elif choice == '0':
            print("Спасибо за использование программы!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите номер задачи.")