def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j],end=" ")
        print()

def find_empty_cell(arr,location):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]==0):
                location[0]=row
                location[1]=col
                return True
    return False

def in_row(arr,row,num):
    for col in range(9):
        if(arr[row][col] == num):
            return True
    return False

def in_col(arr,col,num):
    for row in range(9):
        if(arr[row][col] == num):
            return True
    return False

def in_box(arr,row,col,num):
    for i in range(3):
        for j in range(3):
            if(arr[i+row][j+col] == num):
                return True
    return False

def check_cell_is_safe(arr,row,col,num):
    return not in_row(arr,row,num) and not in_col(arr,col,num) and not in_box(arr,row - row%3,col - col%3,num)

def solve_sudoku(arr):
    location=[0,0]
    if(not find_empty_cell(arr,location)):
        return True
    row=location[0]
    col=location[1]
    for num in range(1,10):
        if(check_cell_is_safe(arr,row,col,num)):
            arr[row][col]=num
            if(solve_sudoku(arr)):
                return True
            arr[row][col] = 0
    return False

if __name__=="__main__":
    grid=[[0 for x in range(9)]for y in range(9)]
    grid=[[0,7,0,0,0,3,4,1,0],
          [0,9,2,0,0,0,0,0,5],
          [1,6,0,7,0,0,8,9,0],
          [0,0,9,2,0,0,0,0,8],
          [2,8,6,0,0,0,1,5,3],
          [5,0,0,0,0,8,9,0,0],
          [0,3,1,0,0,2,0,4,9],
          [6,0,0,0,0,0,5,8,0],
          [0,5,8,6,0,0,0,3,0]]
    if(solve_sudoku(grid)):
        print_grid(grid)
    else:
        print('No solution exists')
