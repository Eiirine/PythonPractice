# Создайте словарь «Рыбы», а его элементы разделите на 3 вида:
# «речные», «озерные» и «морские рыбы». Выведите на экран сначала только ключи, а потом элементы словаря.

fishes = {'River': 'Catfish, Grayling, Roach', 'Lake': 'Pike, Perch, Bream', 'Sea': 'Cod, Herring, Mackerel'}
print(fishes)
for i in fishes:
    print(i)
for i in fishes:
    print(fishes[i])
