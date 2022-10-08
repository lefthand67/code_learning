# 3. Поиск ближайших одинаковых чисел в массиве

lst = [1, 2, 3, 4, 2, 1, 2]
min_x = None

i = 0
while i < len(lst) - 1:
    a = lst[i]
#     print(i, a)
    j = i + 1
    while j < len(lst):
        b = lst[j]
        if a == b:
            x = abs(i - j)
            print('i={0} j={1}: x={2}'.format(i, j, x))
            if min_x is None or min_x > x:
                min_x = x
    i += 1

print('Minimum:', min_x)
print('Done')
