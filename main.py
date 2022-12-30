import random
from os import system

map = [
    '          ', '          ', '          ',
    '          ', '          ', '          ',
    '          ', '          ', '          ',
    '          ', '          ', '          ',
    '----------', '----------', '----------',
    '          ', '          ', '          ',
    '          ', '          ', '          ',
    '          ', '          ', '          ',
    '          ', '          ', '          ',
    '----------', '----------', '----------',
    '          ', '          ', '          ',
    '          ', '          ', '          ',
    '          ', '          ', '          ',
    '          ', '          ', '          ']
X = [
    '   \  /   ',
    '    \/    ',
    '    /\    ',
    '   /  \   ']
O = [
    '   ----   ',
    '  |    |  ',
    '  |    |  ',
    '   ----   ']

moves = {(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2), }

X_moves, O_moves = set(), set()


def Log() -> None:
    for i in range(0, len(map)):
        print(map[i] + '|', end='') if (i-2) % 3 != 0 else print(map[i])


wins = [{(0, 0), (0, 1), (0, 2)},
        {(1, 0), (1, 1), (1, 2)},
        {(2, 0), (2, 1), (2, 2)},
        {(0, 0), (1, 0), (2, 0)},
        {(0, 1), (1, 1), (2, 1)},
        {(0, 2), (1, 2), (2, 2)},
        {(0, 0), (1, 1), (2, 2)},
        {(0, 2), (1, 1), (2, 0)}]


def check(X_O):
    if X_O == X:
        for i in wins:
            if i.issubset(X_moves):
                return "X wins!"
    elif X_O == O:
        for i in wins:
            if i.issubset(O_moves):
                return "O wins!"
    if len(moves) == 0:
        return "Tie game!"


def place(row, col, X_O) -> None:
    if (row, col) in moves:
        for i in range(0, 4):
            map[row*15 + col + i*3] = X_O[i]
        moves.remove((row, col))
        X_moves.add((row, col)) if X_O == X else O_moves.add((row, col))
    else:
        r = input('row : ')
        c = input('column : ')
        while r.isnumeric() == False or c.isnumeric() == False:
            r = input('row : ')
            c = input('column : ')
        place(int(r), int(c), X)
        # AI is always right this condition if only for human


def generate() -> None:
    ai_move = tuple()
    for move in moves:
        Opredicted, Xpredicted = O_moves.copy(), X_moves.copy()
        Opredicted.add(move)
        Xpredicted.add(move)
        for win in wins:
            if win.issubset(Opredicted) or win.issubset(Xpredicted):
                ai_move = move
    if len(ai_move) == 0:
        if (1, 1) in moves:
            ai_move = (1, 1)
        else:
            ai_move = random.choice(tuple(moves))

    place(ai_move[0], ai_move[1], O)


verify = None
while verify == None:
    system('cls')
    Log()
    r = input('row : ')
    c = input('column : ')
    while r.isnumeric() == False or c.isnumeric() == False:
        r = input('row : ')
        c = input('column : ')
    place(int(r), int(c), X)
    verify = check(X)
    if verify : break
    generate()
    verify = check(O)

system('cls')
Log()
print(verify)
