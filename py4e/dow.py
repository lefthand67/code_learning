fhand = open('mbox-short.txt')

for line in fhand:
    data = line.strip()
# searching for @ nsign position
    atpos = data.find('@')

#searching for a space position
    sppos = data.find(' ', atpos)

#extracting the suffix using string slicing
    host = data[atpos+1 : sppos]
    print(host)