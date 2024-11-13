import random
   
def displayBoard1(board):
    
    print("\nMINESWEEPER GAME BOARD")
    print("----------------------")
    print("  0 1 2 3 4 5 6 7 8 9")
    print("----------------------")

    for row in range(len(board)):
        print(row,"|",end=" ")
        
        for col in range(len(board[row])):
            print(board[row][col], end=" ")
        print()


def displayBoard2(board):
    
    print("\n\tMINESWEEPER GAME BOARD")
    print("-----------------------------------")
    print("  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ")
    print("-----------------------------------")

    for row in range(len(board)):
        if row in range(0, 10):
            print(row," |",end=" ")
        else:
            print(row,"|",end=" ")
        
        for col in range(len(board[row])):
            print(board[row][col], end=" ")
            
        print()

def resetBoard1():
    return [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]


def resetBoard2():
    return [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

            
def randomMinesLocations(answerBoard, length):
    for num in range(0, 21):
        mines = [random.randint(0,length),random.randint(0,length)]
        answerBoard[mines[0]][mines[1]] = '*'
        
def getAdjMineCount(answerBoard, row, col):
    count = 0

    rowRange = range(row - 1, row + 2)
    colRange = range(col - 1, col + 2)

    for r in rowRange:
        for c in colRange:
            if 0 <= r < len(answerBoard) and 0 <= c < len(answerBoard[row]) and (r, c) != (row, col) and answerBoard[r][c] == "*":
                count += 1

    if count > 0:
        return str(count) 
    else: 
        return "."
    
def checkWin(count):
    win = True
    while count != 0:
        win = False
        return win


def makeMove(gameBoard, answerBoard, row, col):
    move = answerBoard[row][col]
    if move != "*":
        gameBoard[row][col] = getAdjMineCount(answerBoard, row, col)
        answerBoard[row][col] = getAdjMineCount(answerBoard, row, col)
        print(f"You hit a {move}, you are safe!")
        return 1
    else:
        print ("\nGame Over!!! Better luck next time!")
        return 0

def genAnswerBoard1(answerBoard):

    finalBoard1 = []
    
    for row in range(len(answerBoard)):
        finalRow1 = []

        for col in range(len(answerBoard[row])):
            if answerBoard[row][col] == "*":
                finalRow1.append("♡")
            else:
                adjMineCount = getAdjMineCount(answerBoard, row, col)
                finalRow1.append(adjMineCount)

        finalBoard1.append(finalRow1)

    return displayBoard1(finalBoard1)

def genAnswerBoard2(answerBoard):

    finalBoard2 = []
    
    for row in range(len(answerBoard)):
        finalRow2 = []
        for col in range(len(answerBoard[row])):
            if answerBoard[row][col] == "*":
                finalRow2.append("♡")
            else:
                adjMineCount = getAdjMineCount(answerBoard, row, col)
                finalRow2.append(adjMineCount)

        finalBoard2.append(finalRow2)

    return displayBoard2(finalBoard2)
