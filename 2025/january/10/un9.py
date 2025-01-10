# Даны три числа. Напишите программу, которая выводит количество одинаковых чисел в этой цепочке

a, b, c = map(float, input("Введите 3 числа").split())
count = 0
if a == b == c:
    count = count + 3
elif a == b or b == c or c == a:
    count = count + 2
print("Количество одинаковых чисел: ", count)
