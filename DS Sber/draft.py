fhand = open('task_file.txt', 'r+')

lst = []
for line in fhand:
    line = line.split()
    if len(line) == 5:
        lst.append(line)
print(len(lst))

for line in lst:
    if len(line[1]) <= 1:
        print(line, line[1])
        lst.remove(line)
    # for line in lst:
#         print(line)
# print(len(lst))
