fname = input("Enter file name: ")
fh = open(fname)
list = []
for line in fh:
    word = line.split()
    for i in range(len(word)):
        if word[i] in list:
            continue
        else:
            list.append(word[i])
            
list.sort()
print(list)
