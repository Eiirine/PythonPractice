# Даны ящики, которые вмещают 5 кг, 10 кг и 15 кг яблок. Необходимо выяснить, сколько ящиков разного размера понадобится для
# того, чтобы распределить яблоки.


def crates():
    cratesfifteenkilos = 0
    cratestenkilos = 0
    cratesfivekilos = 0
    while True:
        try:
            apples = int(input("Введите количество яблок: "))
            if apples >=0:
                while apples >= 15:
                    apples -= 15
                    cratesfifteenkilos += 1
                while apples >= 10:
                    apples -= 10
                    cratestenkilos += 1
                while apples >= 5:
                    apples -= 5
                    cratesfivekilos += 1
                print(f"Всего осталось {apples}. Для распределения понадобилось {cratesfifteenkilos} ящиков по 15 килограмм, {cratestenkilos} ящиков по 10 килограмм и {cratesfivekilos} ящиков по 5 килограмм.")
                break
            else:
                print("Ошибка ввода! Пожалуйста, неотрицательное число.")
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите целое число.")

crates()