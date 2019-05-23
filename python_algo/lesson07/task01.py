# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random


def bubble_sort(array):
    for i in range(len(array)):
        is_sorted = True
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = False
        if is_sorted:
            break


if __name__ == '__main__':
    size = 10
    # генерируем
    a = [random.randrange(-100, 100) for _ in range(size)]
    b = a.copy()
    print(a)
    # сортируем
    bubble_sort(a)
    print(a)
    # проверяем
    b.sort()
    print('верно' if a == b else 'не верно')