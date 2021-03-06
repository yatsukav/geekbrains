# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков. Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом,
# ● написать общий вывод: какой из трёх вариантов лучше и почему.
# Использовать timeit и cProfile для анализа.
import timeit

# Задача: Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125...


# Решение №1. Динамическое программирование
# Это решение находит искомые элемент за временную сложность O(N) и использует O(N) объема памяти,
# так как все промежуточные элементы необходимо хранить на стеке до окончания рекурсии.
# Answ	        N	    O(N)	t, sec
# 1	            1	    1	    0.0000014371
# 0.666015625	10	    10	    0.0000041477
# 0.666666666	100	    100	    0.0000286995
# 0.666666666	1000	1000	0.0004637941
def solution1(n):
    import sys
    sys.setrecursionlimit(1500)

    def recursive(elem, deep, k):
        if deep == 1:
            return elem, k
        else:
            elem_, k_ = recursive(elem * -0.5, deep - 1, k + 1)
            return elem + elem_, k_
    return recursive(1, n, 1)


print('=== Решение 1 ===')
print('Answ\tN\tO(N)\tt, sec')
for i in [1, 10, 100, 1000]:
    answer, operation_count = solution1(i)
    duration = timeit.timeit(f'solution1({i})', number=10, setup='from __main__ import solution1') / 10
    print(f'{answer}\t{i}\t{operation_count}\t{duration}')


# Решение №2. Полный перебор элементов
# Это решение находит искомый элемент за временную сложность O(N**2) и использует O(1) объема памяти.
# Answ	        N	    O(N)	t, sec
# 1	            1	    1	    0.0000010025
# 0.666015625	10	    55	    0.0000083481
# 0.666666666	100	    5050	0.0005126643
# 0.666666666	1000	500500	0.0442062837
def solution2(n):
    k = 0
    summ = 0
    for i in range(n):
        k += 1
        elem = 1
        for j in range(i):
            k += 1
            elem /= -2
        summ += elem
    return (summ, k)
print('=== Решение 2 ===')
print('Answ\tN\tO(N)\tt, sec')
for i in [1, 10, 100, 1000]:
    answer, operation_count = solution2(i)
    duration = timeit.timeit(f'solution2({i})', number=10, setup='from __main__ import solution2') / 10
    print(f'{answer}\t{i}\t{operation_count}\t{duration}')


# Решение №3. Перебор элементов с аккумулятором
# Это решение находит искомый элемент за временную сложность O(N) и использует O(1) объема памяти.
# Answ	        N	    O(N)	t, sec
# 1	            1	    1	    0.0000006707
# 0.666015625	10	    10	    0.0000014769
# 0.666666666	100	    100	    0.0000108109
# 0.666666666	1000	1000	0.0001141751
def solution3(n):
    k = 0
    summ = 0
    elem = 1
    for _ in range(n):
        k += 1
        summ += elem
        elem /= -2
    return (summ, k)
print('=== Решение 3 ===')
print('Answ\tN\tO(N)\tt, sec')
for i in [1, 10, 100, 1000]:
    answer, operation_count = solution3(i)
    duration = timeit.timeit(f'solution3({i})', number=10, setup='from __main__ import solution3') / 10
    print(f'{answer}\t{i}\t{operation_count}\t{duration}')


# Решение №4. Геометрическая прогрессия
# Это решение находит искомый элемент за временную сложность O(1) и использует O(1) объема памяти.
# Answ	        N	    O(N)	t, sec
# 1.0	        1	    1	    0.0000003943
# 0.666015625	10	    1	    0.0000003742
# 0.666666666	100	    1	    0.0000003646
# 0.666666666	1000	1	    0.0000003624
def solution4(n):
    return 1 * (1 - (-0.5) ** n) / (1 - (-0.5)), 1
print('=== Решение 4 ===')
print('Answ\tN\tO(N)\tt, sec')
for i in [1, 10, 100, 1000]:
    answer, operation_count = solution4(i)
    duration = timeit.timeit(f'solution4({i})', number=10, setup='from __main__ import solution4') / 10
    print(f'{answer}\t{i}\t{operation_count}\t{duration}')

# Анализ cProfile ######################################################################################################
import cProfile
for i in [1, 2, 3, 4]:
    print(f'=== Решение {i}: cPython ===')
    cProfile.run(f'solution{i}(1000)')

# Вывод: Лучшее решение 4, так как имеет наименьшую временную сложность из представленных.
# Решение 1 имеет линейную сложность, но ограничено памятью и величиной стека из-за использования рекурсии.
# Решение 2 имеет квадратичную сложность из-за вложенного цикла.
# Решение 3, как и решение 1, имеет линейную сложность, но не использует дополнительной памяти, за счет использования
# одного цикла.
# Решение 4 выполняется за постоянное время, так как вычисляет результат по формуле, без перебора,
# что является наилучшим решением из представленных.
