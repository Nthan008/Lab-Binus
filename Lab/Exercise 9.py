letter = ["A", "B", "C", "D", "E", "F", "G", "H"]
board_row = []
board_collumn = []
x=8
for i in range(8) :
    board_collumn.append([])
    x=8
    for j in range(8) :
        if j<8 :
            board_collumn[i].append(letter[j]+str(x))
            x -= 1
        else :
            j = 0
            break
    
print(board_collumn)    