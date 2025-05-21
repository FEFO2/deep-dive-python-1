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
        else: return False
    else: return False   

def new_game():
    global matrix, x_turn, o_turn
    matrix = [["" for _ in range(3)] for x in range(3)]     # Set game matrix defalut 
    x_turn, o_turn = 0, 0    
    return None

def play(num):  
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

# ------------------------------------------------------

welcome() # Welcome message

while True:
    # default settings
    new_game()
    option = input("Choose your option: ")
    if check(option):
        play(option)

    
