f = open('file.prod')
stacks = []
for line in f:
    if line[1] == '1':
        numere = line.split()
        break
stacks_count = int(max(numere))
print(stacks_count)
for i in range(stacks_count): # creez stackurile
    stacks.append([])

f.seek(0)
for line in f:
    if line[1] == '1':
        break
    i = 1
    curr_stack = 0
    while i < len(line) and i < stacks_count * 4: # merg prin rand
        if line[i] != ' ':
            stacks[curr_stack].append(line[i])
        print(line[i])
        i += 4
        curr_stack += 1

for i in range(len(stacks)): # inversam stack-urile - sunt puse invers
    stacks[i].reverse()

print(stacks)


def move_x_from_y_to_z(x, y, z):
    y -= 1
    z -= 1
    crane = []
    for i in range(x):
        crane.append(stacks[y].pop())
    print("Crane before dropping off the crates:", crane)
    crane.reverse()
    print("Reversed crane:", crane)
    for el in crane:
        stacks[z].append(el)


for line in f:
    if line == '\n':
        continue
    line = line.split()
    count = int(line[1])
    from_stack = int(line[3])
    to_stack = int(line[5])
    move_x_from_y_to_z(count, from_stack, to_stack)
    print(stacks)

final = []
for i in range(len(stacks)):
    final.append(stacks[i][len(stacks[i])-1])

print(''.join(final))




