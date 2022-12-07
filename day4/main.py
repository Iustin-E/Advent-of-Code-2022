f = open('file.prod')
cnt = 0
for line in f:
    line = line.strip().split(',')
    for i in range(2):
        line[i] = line[i].split('-')
        for j in range(2):
            line[i][j] = int(line[i][j])
    print(line)
    print(line[0][0],'cu', line[1][0], 'si', line[0][1],'cu', line[1][1])
    if line[0][0] <= line[1][0] and line[0][1] >= line[1][1]:
        cnt += 1
        print("adev")

    elif line[0][0] >= line[1][0] and line[0][1] <= line[1][1]:
        cnt += 1
        print("adev")
print(cnt)
