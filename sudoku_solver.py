#################################################################################################                                                                   
#                                                                                               # 
# Namn: Mathias Hamlet                                                                          #
# Kurs: Inbyggda System 2                                                                       #
# Uppgift: Sudoku Solver                                                                        #
#                                                                                               #
# This python script takes an unsolved sudoku puzzle (pussel.csv) as                            #                                        
# an argument in the commandline. Then the solution gets created in a CSV                       #                                            
# file named solved.csv.                                                                        #
# To be able to make that as a one-liner in the terminal the module                             #                                    
# sys is imported and used: sys.argv[1] where argv[] is a list in that                          #                                        
# module. sys.argv[1] is the argument pussel.csv I passed in the terminal                       #                                        
# as a string.                                                                                  #
#                                                                                               #
#    THIS IS THE ORDER OF THE FUNCTION DEFINITIONS NOT HOW IT IS EXECUTED                       #
# 1. Import sys module.                                                                         #
# 2. Jump into main().                                                                          #
# 3. Passing command line argument sys.argv[1] to the script                                    #                                 
# 4. We define a nested function read_csv_and_split(csv_file).                                  #                                 
#    This reads a CSV file and converts it into a list of lists, where                          #                                        
#    each inner list represents a row in the CSV file and each item                             #                                        
#    in the inner list represents a cell.                                                       #            
# 5. Creating the, board = read_csv_and_split(csv_file_name).                                   #                                    
# 6. Printing the board to console print_board(board).                                          #            
# 7. Finding zeros with the function print_zeros() and saves this to a list.                    #                    
# 8. Checking possible numbers with possible_number(zero_positions), strategy: "Hidden Single". #                                        
# 9. Checking if the number is valid in row, col and 3x3 square is_valid(board, row, col, num). #                                                                
# 10. Writing the board to a CSV file write_board_to_csv(board, file_name).                     #                                            
# 11. Solving the sudoku by repeatedly calling possible_number(zero_positions)                  #                                                
#     updating the board if a valid number is found, and breaking the loop if no valid number   #                                                                
#     is found.                                                                                 #
#                                                                                               #                                                     
#################################################################################################

import sys

def main():

    # Get the filename from the command line arguments 
    csv_file_name = sys.argv[1] 

    # read the csv file and convert it to a list of lists and makes it to integers 
    def read_csv_and_split(csv_file):
        with open(csv_file, "r") as f:
            lines = f.readlines()
        return [[int(num) for num in line.split(",")] for line in lines]    
    
    board = read_csv_and_split(csv_file_name)
    
    # print_board() prints the sudoku when called and the parameter used then is the original variable name board
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
    
    # Find zeros at row and col and save it to a list  
    def find_zeros():
        zero_positions = []
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == 0:
                    zero_positions.append((x,y))
        return zero_positions            
    
    # Checks possible numbers and searches for "Hidden Singles" 
    def possible_number(zero_positions):
      for x, y in zero_positions:
          possible_numbers = [num for num in range(1, 10) if is_valid(board, x, y, num)]
          if len(possible_numbers) == 1:
              return (x, y, possible_numbers[0])
      return None     
    
    # Check if a number is valid in the given position
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
    
    # Write the board to a CSV file
    def write_board_to_csv(board, file_name):
      with open(file_name, 'w') as f:
          for row in board:
              f.write(','.join(map(str, row)) + '\n')
    
    # Get initial zero position
    zero_positions = find_zeros()
    
    #######################################################################
    # while-loop                                                          #
    # Loop until there are no more zero positions.                        #
    # Get a possible number for the first zero position.                  #
    # If a number was found, update the board and get new zero position.  #
    # If no number was found, break the loop.                             #
    #######################################################################
    while zero_positions:
        result = possible_number(zero_positions)
        if result is not None:
            x, y, num = result
            board[x][y] = num
            zero_positions = find_zeros()
        else:
            break

    # Print the board to the console and to a CSV file     
    print_board(board)
    write_board_to_csv(board, "solved.csv")

###################################################################################################    
#                                                                                                 # 
# if __name__ == "__main__":                                                                      #
#    main()                                                                                       #  
#                                                                                                 # 
# This is good practice in Python to make the scripts easier to troubleshoot and be able to       #   
# import your own modules and functions inside those modules. This also signals to a user/reader  #
# that this is a script that is meant to run.                                                     #
###################################################################################################                 
if __name__ == "__main__":
    main()        
    


