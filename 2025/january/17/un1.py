# Напишите программу, которая получает номер месяца и выводит соответствующее ему время года или сообщение об ошибке.

def season_definer():
    while True:
        try:
            month = int(input("Введите номер месяца: "))
            if 1 <= month <= 12:
                if month == 12 or month in [1, 2]:
                    print("Это зимний месяц.")
                elif 3 <= month <= 5:
                    print("Это весенний месяц.")
                elif 6 <= month <= 8:
                    print("Это летний месяц.")
                else:
                    print("Это осенний месяц.")
                break
            else:
                print("Ошибка ввода! Пожалуйста, введите число от 1 до 12.")
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите целое число от 1 до 12.")

season_definer()
