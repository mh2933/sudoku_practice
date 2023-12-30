
# read the csv file and convert it to a list of lists and makes it to integers 
def read_csv_and_split(csv_file):
    with open(csv_file, "r") as f:
        lines = f.readlines()
    return [[int(num) for num in line.split(",")] for line in lines]    

# Prompt the user for the CSV file name
csv_file_name = input("Enter the CSV file name: ")

board =  read_csv_and_split(csv_file_name)

# print board prints the sudoku when called and the parameter used then is the original variable name board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------------------------")

        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")    
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

def write_board_to_csv(board, file_name):
  with open(file_name, 'w') as f:
      for row in board:
          f.write(','.join(map(str, row)) + '\n')


# Get initial zero position
zero_positions = print_zeros()

# Loop until there are no more zero positions
while zero_positions:
    # Get a possible number for the first zero position
    result = possible_number(zero_positions)
    # If a number was found, update the board and get new zero positions 
    if result is not None:
        x, y, num = result
        board[x][y] = num
        zero_positions = print_zeros()

    # If no number was found, break the loop
    else:
        print_board(board)
        write_board_to_csv(board, "solved_sudoku.csv")
        break



