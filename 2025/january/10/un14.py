# Напишите программу, которая получает два целых числа A и B и выводит квадраты всех натуральных чисел в интервале от A до B.


a, b = map(int, input("Введите два целых числа: ").split())
for i in range(a, b + 1):
    print(i ** 2)
