# initial board state 
# -1 => unoccupied space, 0 => space occupied by O, 1 => space occupied by X
# board represented by a 2 dimensional array (or equivalently a 3x3 matrix)
# | 0,0 | 0,1 | 0,2 |
# | 1,0 | 1,1 | 1,2 |
# | 2,0 | 2,1 | 2,2 |
rows = 3 
columns = 3
board_state = [[-1 for j in range(columns)] for i in range(rows)]

# prints the board to the screen according to the board state
def print_board(board_state):
    for i in range(rows):
        for j in range(columns):
            print('|', end = ' ')
            
            if board_state[i][j] == -1:
                print('-', end = ' ')
            elif board_state[i][j] == 0:
                print('O', end = ' ')
            elif board_state[i][j] == 1:
                print('X', end = ' ')

            print('|', end = ' ')      
        print()


# evaluate the board state to determine if there is a winner or not
def evaluate_board_state(board_state):
    # check row winning conditions
    for i in range(rows):
        if board_state[i][0] == board_state[i][1] and board_state[i][1] == board_state[i][2]:
            if board_state[i][0] == 0:
                return -10
            elif board_state[i][0] == 1:
                return 10

    # check columing winning conditions
    for j in range(columns):
        if board_state[0][j] == board_state[1][j] and board_state[1][j] == board_state[2][j]:
            if board_state[0][j] == 0:
                return -10
            elif board_state[0][j] == 1:
                return 10

    # check diagonal winning conditions
    if board_state[0][0] == board_state[1][1] and board_state[1][1] == board_state[2][2]:
        if board_state[0][0] == 0:
            return -10
        elif board_state[0][0] == 1:
            return 10

    if board_state[0][2] == board_state[1][1] and board_state[1][1] == board_state[2][0]:
        if board_state[0][2] == 0:
            return -10
        elif board_state[0][2] == 1:
            return 10

    return 0

def moves_left(board_state):
    for i in range(rows):
        for j in range(columns):
            if (board_state[i][j] == -1):
                return True
            
    return False

def minimax(board_state, depth, is_max):
    score = evaluate_board_state(board_state)
    
    if score == 10:
        return score
    elif score == -10:
        return score
    elif moves_left(board_state) == False:
        return score

    if is_max:
        best = -1000

        for i in range(rows):
            for j in range(columns):
                if board_state[i][j] == -1:
                    board_state[i][j] = 1

                    best = max(best, minimax(board_state, depth + 1, not is_max) - depth)

                    board_state[i][j] = -1
        return best

    elif not is_max:
        best = 1000

        for i in range(rows):
            for j in range(columns):
                if board_state[i][j] == -1:
                    board_state[i][j] = 0

                    best = min(best, minimax(board_state, depth + 1, not is_max) + depth)

                    board_state[i][j] = -1
        
        return best

def findOpponentBestMove(board_state):
    best = 1000
    row = -1
    column = -1

    for i in range(rows):
        for j in range(columns):
            if (board_state[i][j] == -1):
                board_state[i][j] = 0

                move = minimax(board_state, 0, True)

                board_state[i][j] = -1

                if move < best:
                    best = move
                    row = i
                    column = j

    return row, column

def o_turn(board_state):
    row, column = findOpponentBestMove(board_state)
    board_state[row][column] = 0

def x_turn(board_state):
    row, column = input('X: place X at ').split()
    row = int(row)
    column = int(column)

    while (board_state[row][column] != -1):
        print('board is occupied at row ', row,' column ', column)
        row, column = input('X: place X at ').split()
        row = int(row)
        column = int(column)

    board_state[row][column] = 1

def main():
    print('tic tac toe artificial intelligence\n')
    print_board(board_state)
    
    while evaluate_board_state(board_state) == 0 and moves_left(board_state) == True:
        x_turn(board_state)
        print_board(board_state)
        o_turn(board_state)
        print_board(board_state)

    if (evaluate_board_state(board_state) == 10):
        print('player tic tac toe!')
    elif (evaluate_board_state(board_state) == -10):
        print('ai opponent tic tac toe!')
    else:
        print('draw')
    
if __name__ == "__main__":
    main()
