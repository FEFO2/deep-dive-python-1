def new_game():
    matrix = [["" for _ in range(3)] for _ in range(3)]
    x_turn = 0
    o_turn = 0
    x_nums = []
    o_nums = []

def play(num):
    global x_turn, o_turn, x_nums, o_nums, matrix    
    # PARTE 0: CHECK DE VARIABLE CORRECTA
    if not num.isdigit():
       print("\nInvalid option...")
       return False
    choice = int(num) # Si es un digito convertimos a int
    if not 1 <= choice <= 9:
        print("\nInvalid option...")
        return False
    row = (choice -1) // 3
    column = (choice -1) & 3

    if matrix[row][column] != "":
        print("\nOption already taken...")
        return False
    
    if x_turn == o_turn:
        matrix[row][column] = "X"
        x_nums.append(choice)
        x_turn += 1
    else:
        matrix[row][column] = "O"
        o_nums.append(choice)
        o_turn += 1   

    for row in matrix:
        print(row)         

def check_for_winner():
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],     
        [1, 4, 7], [2, 5, 8], [3, 6, 9],     
        [1, 5, 9], [3, 5, 7] ]
    for comb in winning_combinations:
        if set(comb).issubset(set(x_nums)):
            print("\n X Has won the match!")
            return True
        if set(comb).issubset(set(o_nums)):
            print("\n O Has won the match!") 
            return True       