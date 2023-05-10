
import random
import time

def linSearch(list, lenList, key):

    for i in range(0,lenList):
        if list[i] == key:
            return i
    return 'Такого числа нет в списке'

def binarySearch(list, start_element, key):

    end_element = len(list) - 1
    while start_element <= end_element:
        middle_element = start_element + (end_element - start_element) // 2
        if list[middle_element] == key:
            return middle_element
        elif list[middle_element] < key:
            start_element = middle_element + 1
        else:
            end_element = middle_element - 1
    return 'Такого числа нет в списке'


numbers = list(range(10,250000000,random.randint(3,5)))

random_numbers = [random.randint(10, 250000000) for i in range(10)]

start = time.time()
for i in random_numbers:

    result = linSearch(numbers, len(numbers), i)
    if result != 'Такого числа нет в списке':
        print('Числа', i, 'нет в списке.')
    else:
        print('Число', i, 'найдено в списке.')
end = time.time()

print((end - start) * 10**3, 'мс')
print()
print()


start = time.time()
for i in random_numbers:
    result = binarySearch(numbers, 0, i)
    if result != 'Такого числа нет в списке':
        print('Числа', i, 'нет в списке.')
    else:
        print('Число', i, 'найдено в списке.')

end = time.time()

print((end - start) * 10**3, 'мс')