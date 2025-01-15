# Составим программу нахождения всех простых чисел в интервале от 2 до 100.

for num in range (2, 101):
    flag = False
    for k in range (2, num):
        if num % k == 0:
            flag = True
            break
    if not flag:
        print(num)
