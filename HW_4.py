# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

import random

def ls_num(number):
    ls_num = []
    i = 0
    while i < number:
        ls_num.append((round(random.uniform(1, 11),2)))
        i += 1
    return ls_num

def result(ls):
    resalt = []
    i = 0
    while i < len(ls):
        resalt.append(round((ls[i]%1),2))
        i +=1
    max_num = max(resalt)
    min_num = min(resalt)
    diff = max_num-min_num
    # print (resalt)
    return min_num, max_num, diff

num = int(input('Введите количество чисел для списка (от 1 до 10): '))
qwerty = ls_num(num)
print(qwerty)
Min, Max, Diff = result(qwerty)
print(f"Min: {Min}, Max: {Max} Difference: {Diff} ")
