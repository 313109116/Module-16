seq = input("Введи последовательность: ")


l = list(seq)
del l[1::2]

for i in range(len(l)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(l)):
        if l[j] < l[idx_min]:
            # counter+=1
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        l[i], l[idx_min] = l[idx_min], l[i]

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] < element <= array[middle + 1]:
        return middle
    elif element <= array[middle]:
        return binary_search(array, element, left, middle)
    else:
        return binary_search(array, element, middle, right)

#
while True:
    try:

        any_n = True
        any_n = input("Введи число: ")
        break
    except ValueError:
        print('Неверное значение')

if any_n <= min(l) or max(l) < any_n:
        print('Число больше или равно максимальному, либо меньше минимального')


else:
    print(binary_search(l, any_n, 0, len(l)))