# Напишите программу по обмену валюты в сомах, долларах и евро.

def currency_exchange():
    currency = input("Введите вашу валюту (USD, EUR, RUB): ").strip().upper()
    target_currency = input("На какую валюту обменять (USD, EUR, RUB): ").strip().upper()

    if currency == target_currency:
        print("Нельзя обменять валюту на ту же самую.")
        return

    try:
        amount = float(input(f"Введите сумму в {currency}: "))
        if amount < 0:
            print("Сумма не может быть отрицательной.")
            return
    except ValueError:
        print("Пожалуйста, введите корректное число.")
        return

    if currency == "USD" and target_currency == "EUR":
        rate = 0.97
    elif currency == "USD" and target_currency == "RUB":
        rate = 102.29
    elif currency == "EUR" and target_currency == "USD":
        rate = 1.03
    elif currency == "EUR" and target_currency == "RUB":
        rate = 105.0
    elif currency == "RUB" and target_currency == "USD":
        rate = 0.0097
    elif currency == "RUB" and target_currency == "EUR":
        rate = 0.0095
    else:
        print("Обмен между указанными валютами невозможен.")
        return

    converted_amount = amount * rate
    print(f"Вы получили {converted_amount:.2f} {target_currency}.")


currency_exchange()
