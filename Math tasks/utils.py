def get_number(prompt):
    while True:
        user_input = input(prompt)
        normalized_input = user_input.replace(',', '.')
        try:
            return float(normalized_input)
        except ValueError:
            print("Ошибка: Введите корректное число (можно использовать дробную часть, заменяя запятую на точку).")