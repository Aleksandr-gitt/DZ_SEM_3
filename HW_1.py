# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import sample

def form_list(a):
    ls = sample(range(a*2), a)  # *2 для увеличения разнообразия чисел.
    return ls

def sum_elem(num_list, count):
    sum = 0
    for i in range(0,count,2):  # -------------через RANGE--------------
        sum += num_list[i]
    # i = 0                   ----------------через while----------------
    # while i < count:
    #     sum += num_list[i]
    #     i += 2
    return sum

count = int(input('Введите количество чисел для списка: '))
qwerty = form_list(count)
print (qwerty)
print(sum_elem(qwerty, count))
