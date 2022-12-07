f = open("file.in")
'''
A and X - ROCK
B and Y - PAPER
C AND Z - SCISSORS

'''

points = 0
def decide_winner(a, b):    # return punctele pe runda
    if a == 'A':        # ROCK - inamic
        if b == 'X':    # LOSE - SCISSORS
            return 3 + 0
        elif b == 'Y':
            return 1 + 3 # DRAW
        else:
            return 2 + 6 # WIN
    elif a == 'B':      # PAPER
        if b == 'X':
            return 1 + 0
        elif b == 'Y':
            return 2 + 3
        else:
            return 3 + 6
    else:               # SCISSORS
        if b == 'X':
            return 2 + 0
        elif b == 'Y':
            return 3 + 3
        else:
            return 1 + 6


for linie in f:
    runda = 0
    lista = linie.strip().split()
    result = decide_winner(lista[0], lista[1])
    print("-> Bataie:", lista[0], lista[1])
    print(result, 'puncte')
    points += result
print(points)



