#Функция для поиска второго наибольшего числа
import random

nums = [random.randint(1, 100) for _ in range(10)]
print(nums)
def second_largest(nums):
    unique_nums = list(set(nums))
    sorted_nums = sorted(unique_nums, reverse=True)
    return(sorted_nums[1])
print(second_largest(nums))