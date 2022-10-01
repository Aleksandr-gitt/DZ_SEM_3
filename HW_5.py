# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

num = int(input('Введите число: '))

ls = []
ls.append(0)
i = 1
j = 1
while i < num+1:
    if i < 3:
        ls.append(1)
        ls.insert(0, 1*j)
        j *= -1
    else:
        ls.append(ls[-1]+ls[-2])
        ls.insert(0, (ls[1] - ls[0]))
    i +=1

print(ls)