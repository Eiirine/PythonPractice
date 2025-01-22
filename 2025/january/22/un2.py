# Напишите функцию, которая выводит на экран три переданные ей числа в порядке возрастания.

def print_sorted_numbers():
    a, b, c = map(float, input("Введите три числа через пробел: ").split())
    numbers = [a, b, c]
    numbers.sort()
    print("Числа по возрастанию:", numbers)


print_sorted_numbers()
