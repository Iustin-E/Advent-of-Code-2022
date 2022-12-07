f = open('file.prod')
lines = f.readlines()
letters = []
for i in range(len(lines)):
    lines[i] = lines[i].strip()

for i in range(len(lines)//3):  # itereaza prin grupuri
        print(i, lines[i])
        for letter in lines[i*3]: # itereaza prin literele unui element
            if letter in lines[i*3+1] and letter in lines[i*3+2]:
                print(letter)
                if 'a' <= letter <= 'z':
                    letters.append(ord(letter) - 96)
                    break
                else:
                    letters.append(ord(letter) - 38)
                    break
print(sum(letters))


