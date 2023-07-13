def binary_search(array, element, left, right):
    if left > right: # если левая граница превысила правую,
        return False # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle - 1] < element and element <= array[middle]: # если элемент в середине,
        return middle # возвращаем этот индекс
    elif element < array[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else: # иначе в правой
        return binary_search(array, element, middle + 1, right)


def sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


element = int(input("Введите число:"))
number_list = input("Введите числовую последовательность через пробел:")

my_list = []
my_list = number_list.split(" ")
try:
    my_list = list(map(int, my_list))
except ValueError:
    print('Это не числовая последовательность. Выход из программы.')

my_list = sort(my_list)

if element < my_list[0] or element > my_list[-1]:
    print("Условия не удовлетворены, число вышло за пределы списка")
else:
    number_position = binary_search(my_list, element, 0, len(my_list))
    print(number_position)