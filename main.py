# Manar A and Sasha G
# 03/18/24
# Sudoku

# generate_puzzle: Creates a Sudoku puzzle.
def generate_puzzle():
    x = [None] * 9
    
    x[0] = [2,4,3,7," ",1,8,6,9]
    x[1] = [5," ",7,9," "," "," ",3," "]
    x[2] = [" ",1," "," ",4," "," "," ",5]
    
    x[3] = [" ",2," "," ",7," ",5," "," "] 
    x[4] = [3," ",5," "," "," ",2," ",7]
    x[5] = [" "," ",1," ",3," "," ",4," "]
    
    x[6] = [1," "," "," ",9," "," ",7," "]
    x[7] = [" ",6," "," "," ",7,4," ",8]
    x[8] = [7,3,4,5," ",8,6,9,1]
    
    return x

# display_board: Displays the Sudoku board to the console using Unicode characters.
def display_board(board):

    row = 0
    top_line = "  \u250f\u2501\u252f\u2501\u252f\u2501\u2533\u2501\u252f\u2501\u252f\u2501\u2533\u2501\u252f\u2501\u252f\u2501\u2513"
    thin_middle = "  \u2520\u2500\u253c\u2500\u253c\u2500\u2542\u2500\u253c\u2500\u253c\u2500\u2542\u2500\u253c\u2500\u253c\u2500\u2528"
    thick_middle = "  \u2523\u2501\u253f\u2501\u253f\u2501\u254B\u2501\u253f\u2501\u253f\u2501\u254B\u2501\u253f\u2501\u253f\u2501\u252B"
    bot_line = "  \u2517\u2501\u2537\u2501\u2537\u2501\u253B\u2501\u2537\u2501\u2537\u2501\u253B\u2501\u2537\u2501\u2537\u2501\u251b"
    print("\n   \u269e \u2665 ( \u25d5 \u2323 \u25d5 ) \u2665 \u269f\n")
    print("   0 1 2 3 4 5 6 7 8")
    print(top_line)

    # Iterating through rows.
    for r in range(9):

        # Alternating between thin and thick vertical lines between each matrix value.
        count = 0
        print(r, " ", "\u2503", sep="", end="")
        for c in range(9):
            count = count + 1
            print(board[r][c], sep="", end="")
            if (c == 2 or c == 5 or c == 8):
                print("\u2503", sep="", end="")
            else:
                print("\u2502", sep="", end="")

        # Alternating between thin and thick horizontal lines between rows.
        if (r == 2 or r == 5):    
            print("\n", thick_middle, sep="", end="")
        elif (r != 8):
            print("\n", thin_middle, sep="", end="")
        print("\n", sep="", end="")
        if (r == 8):
            print(bot_line)

#Duplicates check
def check_duplicates(board,i,j,k): 
  count = 0 
  for q in range(1,10,1): 
    if(board[i][j] == k):
      count = count + 1;
  return count; 

# duplicate_count: Returns how many times a specific number appears.
def duplicate_count(row, num):
    count = 0
    # Access each row item.
    for r in range(len(row)):
        # If the row item matches num, increment count by 1.
        if (row[r] == num):
            count = count + 1
    return count

# check_row: Returns True if there are no duplicates. False otherwise.
def check_row(b):
    # Access each row.
    for r in range(len(b)):
        # For numbers 1 through 9, count how many times the number appears.
        # If the count is not 1, return False. There are duplicates.
        for n in range(1,10):
            if (duplicate_count(b[r], n) != 1):
                return False
    return True

#Checking each square for duplicates 
def check_square(board):
    for i in range(2):
      for j in range(2): 
        for k in range(1,10,1):
          art = check_duplicates(board,i,j,k); 
          if(art !=1):
            return False; 

    for i in range(2):
      for j in range(3,5,1): 
        for k in range(1,10,1):
          art = check_duplicates(board,i,j,k); 
          if(art !=1):
            return False; 

    for i in range(2):
      for j in range(6,8,1): 
        for k in range(1,10,1):
          art = check_duplicates(board,i,j,k); 
          if(art !=1):
            return False; 

    for i in range(3,5,1):
      for j in range(2): 
        for k in range(1,10,1):
          art = check_duplicates(board,i,j,k); 
          if(art !=1):
            return False; 

    for i in range(3,5,1):
      for j in range(3,5,1): 
        for k in range(1,10,1):
          art = check_duplicates(board,i,j,k); 
          if(art !=1):
            return False; 

    for i in range(3,5,1):
      for j in range(6,8,1): 
        for k in range(1,10,1):
          art = check_duplicates(board,i,j,k); 
          if(art !=1):
            return False; 

    for i in range(6,8,1):
      for j in range(2): 
        for k in range(1,10,1):
          art = check_duplicates(board,i,j,k); 
          if(art !=1):
            return False; 

    for i in range(6,8,1):
      for j in range(3,5,1): 
        for k in range(1,10,1):
          art = check_duplicates(board,i,j,k); 
          if(art !=1):
            return False; 

    for i in range(6,8,1):
      for j in range(6,8,1): 
        for k in range(1,10,1):
          art = check_duplicates(board,i,j,k); 
          if(art !=1):
            return False; 

    return True;

# empty: Returns True if a board row/column location is empty. Returns False otherwise.
def empty(b, r, c):
    # b: 9x9 matrix
    # r: row
    # c: column
    if (b[r][c] == " "):
        return True
    return False

# place_num: Places a number in board row/column location.
def place_num(b, r, c, num):
    b[r][c] = num

# main: Runs the main program.
def main():
    print("Welcome to Sudoku.")
    b = generate_puzzle()
    display_board(b)
    count =0
    while (True):
      print("Please select and index row and column to place a number"); 
      row = int(input("Row: "))
      col = int(input("Column: "))
      num = int(input("Number: "))
      place_num(b, row, col, num)
      display_board(b)
      count = count +1 
      if(count >= 5):
        duplicates_found = check_square(b) 
        if(duplicates_found):  
          display_board(b) 
          continue 
        if(not duplicates_found): 
          print("sorry there is a duplicate")
          break

main()