# У героя Майнкрафта Алекса есть машина, которая выпускает по 4 минерала в минуту.
# На каждые 100 минералов можно построить новую машину, которая также выпускает по 4 минерала в минуту.
# Напишите программу, которая вычислит, сколько машин будет у Алекса через час.

machines = 1
minerals = 0
production_rate = 4
minerals_for_new_machine = 100

for minute in range(1, 61):
    minerals += machines * production_rate

    while minerals >= minerals_for_new_machine:
        minerals -= minerals_for_new_machine
        machines += 1
        
print(f"Через час у Алекса будет {machines} машин")
