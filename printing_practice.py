board = [
            [0,5,9,7,3,2,8,6,1],
            [6,0,1,0,0,0,0,0,3],
            [0,8,0,6,9,1,0,7,5],
            [0,9,7,0,2,8,5,3,0],
            [0,6,0,1,7,0,0,0,4],
            [0,2,4,0,5,6,7,1,0],
            [2,0,8,9,0,4,6,0,7],
            [0,0,0,5,8,3,0,9,0],
            [0,0,0,0,6,7,3,4,8]
]

# print board prints the sudoku when called and the parameter used then is the original variable name board
def print_board(bo_parameter):
    for i in range(len(bo_parameter)):
        if i % 3 == 0 and i != 0:
            print("------------------------")

        for j in range(len(bo_parameter)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo_parameter[i][j])
            else:
                print(str(bo_parameter[i][j]) + " ", end="")    
        #print(len(bo_parameter[1]))                

# print zeros row and column 
def print_zeros():
    zero_positions = []
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 0:
                zero_positions.append((x,y))
                #print(f"rad: {x} kol: {y}")
                #return board[x][y]
    return zero_positions            

#print_zeros()

def possible_number(zero_positions):
    #zero_positions = print_zeros()
    for x, y in zero_positions:
        for num in range(1, 10):
            if is_valid(board, x, y ,num):
                print(possible_number(zero_positions))
                return (x, y, num)
    return None    


def is_valid(board, row, col, num):
    for x in range(len(board[0])):
        if board[row][x] == num:
            return False
        
    for x in range(len(board)):
        if board[x][col] == num:
            return False

    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True  


zero_positions = print_zeros()
print(possible_number(zero_positions))
# print(zero_positions)

                  

#print(possible_number())


#print_board(board)

