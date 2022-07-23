import random

def random_number():
    return round(random.randint(1, 100) / 10) * 10

def sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

array = []

for i in range(10):
    array.append(random_number())

print(sort(array))
