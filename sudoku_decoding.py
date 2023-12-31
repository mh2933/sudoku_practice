import time

# Read the CSV file and convert it to a list of lists and make it integers
def read_csv_and_split(csv_file):
  with open(csv_file, "r") as f:
      lines = f.readlines()
  return [[int(num) for num in line.split(",")] for line in lines]

board = read_csv_and_split("input_sudoku.csv")
print("CSV file read successfully.\n")
time.sleep(1)

# Print board prints the sudoku when called and the parameter used then is the original variable name board
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

# Print zeros row and column
def find_zeros():
  zero_positions = []
  for x in range(len(board)):
      for y in range(len(board)):
          if board[x][y] == 0:
              zero_positions.append((x,y))
  return zero_positions

def possible_number(zero_positions):
   for x, y in zero_positions:
       possible_numbers = []
       for num in range(1, 10):
           if is_valid(board, x, y, num):
               possible_numbers.append(num)
       print(f"at position: ({x},{y})")
       print(f"possible numbers: {possible_numbers}")
       print(f"zero_positions: {zero_positions}")
       if len(possible_numbers) == 1:
           print("Hidden Single found")
           return (x, y, possible_numbers[0])
   return None

# Check if a number is valid in the given position
def is_valid(board, row, col, num):
  for i in range(len(board[0])):
      print(f"board[row][i]: ({board[row][i]}, num:{num}")
      if board[row][i] == num:
          return False

  for i in range(len(board)):
      if board[i][col] == num:
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
print("Zero positions found.\n")
time.sleep(1)

# Loop until there are no more zero positions
while zero_positions:
 # Get a possible number for the first zero position
 result = possible_number(zero_positions)
 print("result = possible_number(zero_position)")
 # If a number was found, update the board and get new zero positions
 if result is not None:
     x, y, num = result
     board[x][y] = num
     print(f"Valid number {num} found for position ({x},{y}). Board updated.\n")
     print_board(board)
     print(f"len(board[0]){len(board[0])}")
     print(f"len(board){len(board)}")
     time.sleep(1) # Pause for 1 second
     zero_positions = find_zeros()
 # If no number was found, remove the current zero position and continue with the next one
 else:
     del zero_positions[0]
     print(f"No valid number found for position {zero_positions[0]}. Continuing with the next position...\n")
     time.sleep(1) # Pause for 1 second
