def rectangle():
    try:
        a, b = map(float, input('Введите ширину и высоту треугольника через пробел: ').split())
        if a > 0 and b > 0:
            s = a * b
            print('Площадь прямоугольника: ', s)
        else:
            print("Ошибка! Ширина и высота должны быть положительными числами.")
    except ValueError:
        print("Ошибка ввода! Пожалуйста, введите числа.")

def triangle():
    while True:
        try:
            a, h = map(float, input('Введите основание и высоту треугольника через пробел: ').split())
            if a > 0 and h > 0:
                s = 0.5 * a * h
                print('Площадь треугольника: ', s)
                break
            else:
                print("Ошибка! Основание и высота должны быть положительными числами.")
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите два положительных числа через пробел.")

def area():
    while True:
        figure = input("Выберите фигуру 'прямоугольник' или 'треугольник': ").strip().lower()
        if figure == 'прямоугольник':
            rectangle()
            break
        elif figure == 'треугольник':
            triangle()
            break
        else:
            print("Ошибка ввода! Пожалуйста, выберите 'прямоугольник' или 'треугольник'.")

area()
