# Напишите функцию, которая находит наибольший общий делитель двух натуральных чисел

def greater_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1, num2 = map(int, input("Введите два числа через пробел: ").split())

if num1 > 0 and num2 > 0:
    result = greater_common_divisor(num1, num2)
    print(f"Наибольший общий делитель чисел {num1} и {num2} равен {result}.")
else:
    print("Ошибка ввода! Вводите только натуральные числа.")
