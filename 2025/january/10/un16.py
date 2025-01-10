# Дан брусок длиной 20 метров. Напишите программу, которая посчитает, какое минимальное целое количество отрезков длиной 1,5 м и 2 м получится из данного бруска.

def log_segments():
    log_length = int(input("Введите длину бревна: "))
    if log_length < 0:
        print("Длина бревна не может быть отрицательной.")
        return
    segments = log_length / 2.0
    if log_length % 2 >= 1.5:
        segments += 1
    print(f"Количество сегментов: {int(segments)}")

log_segments()