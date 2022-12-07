f = open('file.prod')
cnt = 0
for line in f:
    line = line.strip().split(',')
    for i in range(2):
        line[i] = line[i].split('-')
        for j in range(2):
            line[i][j] = int(line[i][j])
    print(line)
    elf1 = []
    for i in range(line[0][0], line[0][1]+1):
        elf1.append(i)
    for i in range(line[1][0], line[1][1]+1):
        if i in elf1:
            print("overlap")
            cnt += 1
            break
    #print("Elf 1:", elf1)
    #print("Elf 2:", elf2)
print(cnt)