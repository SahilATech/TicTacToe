user = input("Enter cells:")
sep_line = "-" * len(user)
print(sep_line)

for i in range(0,8,3):
    print(f"| {user[i]} {user[i+1]} {user[i+2]} |")
print(sep_line)

def findHorizontal(value,player):  # Horizontal
    for i in range(0,8,3):
        if value[i] == player and value[i+1] == player and value[i+2] == player:
            return True
def findVertical(value,player):  # Vertical
    for x in range(0,3):
        if value[x] == player and value[x+3] == player and value[x+6] == player:
            return True
def findDiagonal(value,player):  # Diagonal
    if value[0] == player and value[4] == player and value[8] == player:
        return True
    elif value[2] == player and value[4] == player and value[6] == player:
        return True

hO = findHorizontal(user,"O")
hX = findHorizontal(user,"X")

vO = findVertical(user,"O")
vX = findVertical(user,"X")

dO = findDiagonal(user,"O")
dX = findDiagonal(user,"X")

count_x,count_o,count_under = 0, 0, 0

for i in range(0,9):
    if user[i] == "X":
        count_x += 1
    elif user[i] == "O":
        count_o += 1
    elif user[i] == "_":
        count_under += 1

if (hO == True or vO == True or dO == True) and (hX == True or vX == True or dX == True):
    print("Impossible")
elif (count_x - count_o) > 1 or (count_o - count_x) > 1:
    print("Impossible")
elif hO == True or vO == True or dO == True:
    print("O wins")
elif hX == True or vX == True or dX == True:
    print("X wins")
elif count_under > 0:
    print("Game not finished")
else: 
    print("Draw")
