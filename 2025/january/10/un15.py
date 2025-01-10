# Дано натуральное число. Напишите программу, которая находит сумму его цифр.

num = str(input("Введите число: "))
i = len(num)
digit_sum = 0
for i in range(0, i):
    digit_sum += int(num[i])
print(digit_sum)
