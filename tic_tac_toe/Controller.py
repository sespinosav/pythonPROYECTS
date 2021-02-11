from Board import Board 

board = Board()

print()
print("START x AND THEN o")
print()
entry = 1
l = "o"

while entry:
    if l == "o":
        l = "x"
    else:
        l = "o"

    print()
    board.paint()
    print()
    entry = input()
    try:
        entry = int(entry)
        if entry >= 0 and entry <= 8:
            board.set(entry,l)
            if entry == 0:
                entry = True
        else:
            entry = False
    except:
        entry = False
