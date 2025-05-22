def welcome():
    print()
    print()
    print("---------------------------")
    print("Welcome to TicTacToe 2000!")
    print("---------------------------")
    print()
    print()

def check(num):
    if num.isdigit():
        choice = int(num)
        if 1 <= choice <= 9:
            return True
        else:
            print("Invalid option...") 
            return False
    else: 
        print("Invalid option...")
        return False   

def new_game():
    global matrix, x_turn, o_turn
    matrix = [["" for _ in range(3)] for x in range(3)]     # Set game matrix defalut 
    x_turn, o_turn = 0, 0    
    return None


def play(num):  
    global x_turn, o_turn
    num = int(num)
    if x_turn == o_turn: # Aquí decide si juegan 'X' o 'O'
        if  1 <= num <= 3:
            matrix[0][num-1] = "X"
        elif  4 <= num <= 6:
            matrix[1][num-4] = "X"
        elif  7 <= num <= 9:
            matrix[2][num-7] = "X"
        x_turn += 1
    else:
        if  1 <= num <= 3:
            matrix[0][num-1] = "O"
        elif  4 <= num <= 6:
            matrix[1][num-4] = "O"
        elif  7 <= num <= 9:
            matrix[2][num-7] = "O"
        o_turn += 1
    for row in matrix:
        print(row)
    print()
    if x_turn == o_turn: # Bucle para elegir quien juega
        print("Now plays X!")
    else: print("Now plays O!")    


def check_for_winner():
    win_options = [ [[1,0,0],[1,0,0],[1,0,0]],  # write all win positions
                [[0,1,0],[0,1,0],[0,1,0]],
                [[0,0,1],[0,0,1],[0,0,1]],
                [[1,1,1],[0,0,0],[0,0,0]],
                [[0,1,0],[0,1,0],[0,1,0]],
                [[0,0,1],[0,0,1],[0,0,1]],
                [[1,0,0],[0,1,0],[0,0,1]],
                [[0,0,1],[0,1,0],[1,0,0]]]
    check_x = [[1 if x == "X" else 0 for x in line] for line in matrix]
    check_o = [[1 if x == "X" else 0 for x in line] for line in matrix]
    for option in win_options:
        if check_x == option:
            print("Winner is X!")
        if check_o == option:
            print("Winner is O!")

# ------------------------------------------------------

welcome() # Welcome message

while True:
    # default settings
    new_game()
    while check_for_winner() == None:
        option = input("Choose your option from 1 to 9: ")
        if check(option):
            play(option)
            check_for_winner()

    
