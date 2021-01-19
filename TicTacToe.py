from string import digits

def check(sign):
    for i in range(3):
        #check each Row for Win        #check each Column for win       #check each Diagonal for win
        if m[i][0] == m[i][1] == m[i][2] == sign \
        or m[0][i] == m[1][i] == m[2][i] == sign \
        or m[0][0] == m[1][1] == m[2][2] == sign \
        or m[0][2] == m[1][1] == m[2][0] == sign:
            return True
         
def big_check():
        global condition
        
        global condition
        if check("X"):
            print("X wins")
            condition = False
        elif check("O"):
            print("O wins")
            condition = False
        elif "_" not in m[0] and "_" not in m[1] and "_" not in m[2]:
            print("Draw")
            condition = False
            
            
def print_board():
      print(f"""---------
| {m[0][0]} {m[0][1]} {m[0][2]} |
| {m[1][0]} {m[1][1]} {m[1][2]} |
| {m[2][0]} {m[2][1]} {m[2][2]} |
---------""")
        
        
        
m = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

print(f"""---------
| {m[0][0]} {m[0][1]} {m[0][2]} |
| {m[1][0]} {m[1][1]} {m[1][2]} |
| {m[2][0]} {m[2][1]} {m[2][2]} |
---------""")


coodinates = ["1", "2", "3"]
turn = 0             #even turn X and Odd Turn O
sign = ""            #According to turn
condition = True        

while condition:
    user_move = input("Enter the coordinates: ").split()
    if turn % 2 == 0:
        sign = "X"

        if m[0][0] == "_" and user_move[0] == "1" and user_move[1] == "1":
            m[0][0] = sign
            print_board()
            big_check()

        elif m[0][1] == "_" and user_move[0] == "1" and user_move[1] == "2":
            m[0][1] = sign
            print_board()
            big_check()


        elif m[0][2] == "_" and user_move[0] == "1" and user_move[1] == "3":
            m[0][2] = sign
            print_board()
            big_check()

        elif m[1][0] == "_" and user_move[0] == "2" and user_move[1] == "1":
            m[1][0] = sign
            print_board()
            big_check()


        elif m[1][1] == "_" and user_move[0] == "2" and user_move[1] == "2":
            m[1][1] = sign
            print_board()
            big_check()


        elif m[1][2] == "_" and user_move[0] == "2" and user_move[1] == "3":
            m[1][2] = sign
            print_board()
            big_check()


        elif m[2][0] == "_" and user_move[0] == "3" and user_move[1] == "1":
            m[2][0] = sign
            print_board()
            big_check()


        elif m[2][1] == "_" and user_move[0] == "3" and user_move[1] == "2":
            m[2][1] = sign
            print_board()
            big_check()


        elif m[2][2] == "_" and user_move[0] == "3" and user_move[1] == "3":
            m[2][2] = sign
            print_board()
            big_check()


        elif str(user_move[0]) and str(user_move[1]) not in digits:
            print("You should enter numbers!")
            continue

        elif user_move[0] and user_move[1] not in coodinates:
            print("Coordinates should be from 1 to 3!")
            continue

        else:
            print("This cell is occupied! Choose another one!")
            continue
    else:
        sign = "O"

        if m[0][0] == "_" and user_move[0] == "1" and user_move[1] == "1":
            m[0][0] = sign
            print_board()
            big_check()

        elif m[0][1] == "_" and user_move[0] == "1" and user_move[1] == "2":
            m[0][1] = sign
            print_board()
            big_check()


        elif m[0][2] == "_" and user_move[0] == "1" and user_move[1] == "3":
            m[0][2] = sign
            print_board()
            big_check()

        elif m[1][0] == "_" and user_move[0] == "2" and user_move[1] == "1":
            m[1][0] = sign
            print_board()
            big_check()


        elif m[1][1] == "_" and user_move[0] == "2" and user_move[1] == "2":
            m[1][1] = sign
            print_board()
            big_check()


        elif m[1][2] == "_" and user_move[0] == "2" and user_move[1] == "3":
            m[1][2] = sign
            print_board()
            big_check()


        elif m[2][0] == "_" and user_move[0] == "3" and user_move[1] == "1":
            m[2][0] = sign
            print_board()
            big_check()


        elif m[2][1] == "_" and user_move[0] == "3" and user_move[1] == "2":
            m[2][1] = sign
            print_board()
            big_check()


        elif m[2][2] == "_" and user_move[0] == "3" and user_move[1] == "3":
            m[2][2] = sign
            print_board()
            big_check()

        elif str(user_move[0]) and str(user_move[1]) not in digits:
            print("You should enter numbers!")
            continue

        elif user_move[0] and user_move[1] not in coodinates:
            print("Coordinates should be from 1 to 3!")
            continue


        else:
            print("This cell is occupied! Choose another one!")
            continue

    turn += 1
