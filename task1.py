def algorithm(user_input):
    try:
        user_input = float(user_input)
        return "Привет" if user_input > 7 else ""
    except ValueError:
        try:
            lst = user_input.split()
            return list(filter(lambda x: float(x) % 3 == 0, lst))
        except ValueError:
            return "Привет, Вячеслав" if user_input == "Вячеслав" else "Нет такого имени"


print(algorithm(input("Введите число, строку или массив чисел(числа через пробел) для обработки: ")))
