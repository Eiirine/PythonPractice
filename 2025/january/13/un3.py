# Написать игру, в которой пользователь должен угадать число, загаданное компьютером.

import random

# Рандомизация результата
number = random.randint(1, 10)
choices = 0
while choices < 3:
    # Ввод пользователя
    guess = int(input("Угадайте число от 1 до 10 с трех раз: "))
    # Проверка диапазона ввода
    if guess < 1 or guess > 10:
        print("Пожалуйста, введите число от 1 до 10.")
        continue
    # Проверка результата
    if number != guess:
        hint = "меньше" if guess > number else "больше"
        if choices < 2:
            print(f"Неверно! Осталось {2 - choices} попыток. Подсказка: загаданное число {hint}")
        choices += 1
        if choices == 3:
            print(f"Вы исчерпали все попытки. Загаданное число было {number}. Попробуйте снова!")
    elif number == guess:
        print(f"Поздравляем! Вы угадали число с {choices+1} попытки!")
        break
