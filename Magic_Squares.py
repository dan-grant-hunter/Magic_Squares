# ------------------------- Magic Squares --------------------------------

# Ask user how big the grid is to be
def inputNumber():
  while True:
    try:
       startingNum = int(input('\nEnter a number for the size of the square: '))
       if startingNum <= 1:
           print('\nNumber must be 2 or higher')
           continue
    except ValueError:
       print("\nNot an integer! Try again.")
       continue
    else:
       print()
       return startingNum
       break


# Create an empty array for on screen visuals
def createEmptyArray(startingNum):
    matrix = []
    seperator = " | "
    for cell in range(startingNum):
        row = []
        for cell in range(startingNum):
            row.append('-')
        rowString = map(str, row)
        print(seperator.join(rowString))
        matrix.append(row)
    print()
    return matrix


# Insert user input into empty array onscreen
def insertIntoArray(arrayStartingNum, empty_array):
    matrix = []
    seperator = " | "
    user_input = 1
    for numberx in range(arrayStartingNum):
        row = []
        for numbery in range(arrayStartingNum):
            while True:
                try:
                    num_input = int(input(f'Enter a number for position {user_input}: '))
                    print()
                    if num_input <= 0:
                        print('Number must be 1 or higher\n')
                        continue
                except ValueError:
                    print("\nNot an integer! Try again.\n")
                    continue
                else:
                    row.append(num_input)
                    empty_array[numberx][numbery] = num_input
                    user_input += 1
                    for currentRow in range(arrayStartingNum):
                              converted = map(str, empty_array[currentRow])
                              print(seperator.join(converted))
                    print()
                    break
        matrix.append(row)
    return matrix


# Check Rows
def checkRows(rowMatrix, rowMagicNumber):
    for row in range(len(rowMatrix)):
        if sum(rowMatrix[row]) == rowMagicNumber:
            if row < len(rowMatrix)-1:
               continue
            return True
        return False


# Check Columns
def checkCols(colMatrix, colMagicNumber):
    for col in range(len(colMatrix)):
        if sum(row[col] for row in colMatrix) == colMagicNumber:
            if col < len(colMatrix)-1:
               continue
            return True
        return False


# Check Diagonals
def checkDiags(diagMatrix, diagMagicNumber):
    DiagOne = 1
    DiagTwo = 2
    if sum(diagMatrix[i][i] for i in range(len(diagMatrix))) == diagMagicNumber:
        if sum(diagMatrix[i][len(diagMatrix)-i-1] for i in range(len(diagMatrix))) == diagMagicNumber:
            return True
        return False
    return False


# Main Game Loop
def mainGameLoop():
    # Print variables
    magic = 'This is a Magic Square\n'
    not_magic = 'This is not a Magic Square\n'
    # Ask user for num of grid size
    startingNum = inputNumber()
    # Create empty array and display
    empty_array = createEmptyArray(startingNum)
    # Replace matrix indexes with user input
    matrix = insertIntoArray(startingNum, empty_array)
    # Check what magic number is
    magic_number = sum(matrix[0])
    # Run row, column and diagonals checks
    if checkRows(matrix, magic_number) and checkCols(matrix, magic_number) and checkDiags(matrix, magic_number):
        print(magic)
    else:
        print(not_magic)


# Call Main Game
if __name__ == '__main__':
    while True:
        mainGameLoop()
        while True:
            answer = input('Play again? (Y/N): ')
            if answer.upper() in ('Y', 'N'):
                break
            print('\nInvalid input\n')
        if answer.upper() == 'Y':
            continue
        else:
            print('\nThanks for playing')
            break
