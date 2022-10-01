# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]
from random import sample

def form_list(a):
    ls = sample(range(1, a*2), a)  # *2 для увеличения разнообразия чисел.
    return ls

def new_elem(num_list, num):
    ls_sum = []
    i = 0
    j = -1
    count = num // 2
    if num % 2 == 0:
        while i < count:
            ls_sum.append(num_list[i] * num_list[j])
            i += 1
            j -= 1
    else:
        while i < count:
            ls_sum.append(num_list[i] * num_list[j])
            i += 1
            j -= 1
        ls_sum.append(num_list[count])
    return ls_sum



num = int(input('Введите количество чисел для списка: '))
qwerty = form_list(num)
print(qwerty)
print(new_elem(qwerty, num))





exit()
ls_sum = []
j = 0
k = -1
count = num // 2
if num % 2 == 0:
    while j < count:
        ls_sum.append(ls_num[j]*ls_num[k])
        j += 1
        k -= 1
else:
    while j < count:
        ls_sum.append(ls_num[j]*ls_num[k])
        j += 1
        k -= 1
    ls_sum.append(ls_num[count])
print(ls_sum)