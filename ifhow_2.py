words_num = {
    'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4,
    'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9,
    'десять': 10
}

def convert_to_number(input_value):
    try:
        return int(input_value)
    except ValueError:
        return words_num.get(input_value.lower(), None)

num1_input = input("Введите первое число: ")
num2_input = input("Введите второе число: ")
num3_input = input("Введите третье число: ")

num1 = convert_to_number(num1_input)
num2 = convert_to_number(num2_input)
num3 = convert_to_number(num3_input)

if num1 is None or num2 is None or num3 is None:
    print("Ошибка: введено некорректное значение.")
else:
    if num1 == num2 == num3:
        print(3)
    elif num1 == num2 or num2 == num3 or num1 == num3:
        print(2)
    else:
        print(0)