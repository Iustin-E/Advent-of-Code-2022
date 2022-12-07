f = open("file.prod")
mistakes = []
for line in f:
    print("-" * 30)
    h1 = []
    h2 = []
    line = line.strip()
    for i in range(len(line)//2):
        h1.append(line[i])
    for i in range(len(line)//2, len(line)):
        h2.append(line[i])
    print(h1)
    print(h2)
    for el in h1:
        if el in h2:
            if 'a' <= el <= 'z':
                print(el, ord(el)-96)
                mistakes.append(ord(el)-96)
                break
            else:
                print(el, ord(el)-38)
                mistakes.append(ord(el)-38)
                break
print(sum(mistakes))
