# Программа "Сортировка по ведрам"

arr = [11, 9, 21, 8, 17, 19, 13, 1, 24, 12]
arr_sorted = []

maximum = max(arr)
minimum = min(arr)

if len(arr) % 2 != 0:
    bucket_count = round(len(arr)/2)
else:
    bucket_count = len(arr)/2
step = (maximum - minimum) / bucket_count
bucket_arr = []

print("Начальный массив:")
print(arr)


for i in range(int(bucket_count)):
    bucket_arr.append([])
print("\nПустые корзины:")
print(bucket_arr)

for i in range(len(bucket_arr)):
    for j in range(len(arr)):
        if (arr[j] < int(step*i + step)) and (arr[j] >= int(step*i)):
            bucket_arr[i].append(arr[j])
print("Заполненные корзины:")
print(bucket_arr)

for i in range(len(bucket_arr)):
    bucket_arr[i].sort()
print("Отсортированные корзины:")
print(bucket_arr)

for i in range(len(bucket_arr)):
    for j in range(len(bucket_arr[i])):
        arr_sorted.append(bucket_arr[i][j])

print("\nКонечный массив")
print(arr_sorted)
