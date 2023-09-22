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

def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("------------------------")

        for j in range(len(bo)):
            
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")    
        #print(len(bo[1]))                

def print_zeros():
    
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 0:
                print(x,y)

#def solve():                
    

print_zeros()
#print_board(board)

