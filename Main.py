#Import Minesweeper.py to run properly, or else undefined functions will cause errors and code will not run

import Minesweeper
import random

def main():
    
    gameBoard1 = Minesweeper.resetBoard1()

    answerBoard1 = Minesweeper.resetBoard1()
    
    gameBoard2 = Minesweeper.resetBoard2()
    
    answerBoard2 = Minesweeper.resetBoard2()
    
    selection = "a"
    bGamesPlayed = 0
    iGamesPlayed = 0
    bGamesWon = 0
    iGamesWon = 0

    while selection != "q":
        print("\nMINE SWEEPER GAME")
        print("-------------------------")
        print("i) Display Game Instructions")
        print("p) Play Game")
        print("s) Print Statistics and Save to a File")
        print("q) Quit")
        selection = input("\nPlease make a selection: ")

        
        if selection == "i":
            # print Display Game Instructions
            print("\n\t\t\t\tWELCOME TO MINESWEEPER!\n")
            print("1.) To play Minesweeper, your goal is to reveal all empty squares on the grid without triggering any bombs.")
            print("\n2.) You'll input the row and column numbers of a square you believe does not contain a bomb.")
            print("\n3.) When you select a square, the game will either reveal a number indicating adjacent bombs or mark the square with a '.' if there are no adjacent bombs.")
            print("\n4.) If a square contains a bomb and you select it, the game is lost, and all bombs and adjacent numbers are displayed.")
            print("\n5.) Use your strategy skills to deduce potential bomb locations and systematically reveal squares, aiming for a successful completion of the grid while avoiding bombs.")
            print("\n6.) Have fun and good luck!")
            
        elif selection == "p":
            checkLoss = 1
            
            levelPlayed = input("\nPlease enter if you would like to play at the Beginner level(B) or the Intermediate level (I): ")
            levelPlayed = levelPlayed.upper()
            
            while levelPlayed != "B" and levelPlayed != "I":
                print("\nInvalid selection! Please enter 'B' for beginner level or 'I' for intermediate level.")
                levelPlayed = input("\nPlease enter if you would like to play at the Beginner level(B) or the Intermediate level (I): ")
                levelPlayed = levelPlayed.upper()
            
            if levelPlayed == "B":
                
                bGamesPlayed = bGamesPlayed + 1
                count = len(gameBoard1) * len(gameBoard1) - 20 
                Minesweeper.randomMinesLocations(answerBoard1, 9)
                
                while Minesweeper.checkWin(count) == False and checkLoss == 1:
                    count -= 1
                    Minesweeper.displayBoard1(gameBoard1)
                    userInputRow = int(input("\nPlease enter the row based on the board: "))
                    
                    while userInputRow < 0 or userInputRow > 9:
                        print("\nInvalid Selection!")
                        userInputRow = int(input("\nPlease enter the row based on the board: "))
                        
                    userInputCol = int(input("Please enter the column based on the board: "))
                    
                    while userInputCol < 0 or userInputCol > 9:
                        print("\nInvalid Selection!")
                        userInputCol = int(input("\nPlease enter the column based on the board: "))
                
                    checkLoss = Minesweeper.makeMove(gameBoard1, answerBoard1, userInputRow, userInputCol)
                
                if Minesweeper.checkWin(count) == True:
                    bGamesWon += 1
                    count = 0
                Minesweeper.genAnswerBoard1(answerBoard1)
                gameBoard1 = Minesweeper.resetBoard1()
                answerBoard1 = Minesweeper.resetBoard1()
                
            elif levelPlayed == "I":
                
                iGamesPlayed += 1
                count = len(gameBoard2) * len(gameBoard2) - 20 
                Minesweeper.randomMinesLocations(answerBoard2, 14)

                while Minesweeper.checkWin(count) == False and checkLoss == 1:
                    count -= 1
                    Minesweeper.displayBoard2(gameBoard2)

                    userInputRow = int(input("\nPlease enter the row based on the board: "))
                    
                    while userInputRow < 0 or userInputRow > 14:
                        print("\nInvalid Selection!")
                        userInputRow = int(input("\nPlease enter the row based on the board: "))
                        
                    userInputCol = int(input("Please enter the column based on the board: "))
                    
                    while userInputCol < 0 or userInputCol > 14:
                        print("\nInvalid Selection!")
                        userInputCol = int(input("\nPlease enter the column based on the board: "))
                
                    checkLoss = Minesweeper.makeMove(gameBoard2, answerBoard2, userInputRow, userInputCol)
                    
                if Minesweeper.checkWin(count) == True:
                    iGamesWon += 1
                    count = 0
                Minesweeper.genAnswerBoard2(answerBoard2)
                gameBoard2 = Minesweeper.resetBoard2()
                answerBoard2 = Minesweeper.resetBoard2()
            
        elif selection == "s":
            
            average = 0
            totalGamesPlayed = bGamesPlayed + iGamesPlayed
            bPercentWon = 0
            iPercentWon = 0

            if bGamesPlayed != 0:
                if bGamesWon != 0:
                    bPercentWon = bGamesWon / bGamesWon
            else:
                print("\nYou cannot divide by zero! GO WIN A GAME😡😡")
            
            if iGamesPlayed != 0:
                if iGamesWon != 0:
                    iPercentWon = iGamesPlayed / iGamesWon
            else:
                print("\nYou cannot divide by zero! GO WIN A GAME😡😡")

            totalGamesWon = bGamesWon + iGamesWon
    
            if totalGamesWon != 0:
                average = totalGamesWon/totalGamesPlayed
                
    
            if average < 50:
                description = "horrible score! Do better. 😡"
            else: 
                description = "fantastic score! You're really good at this game! 😊"

            
            print("\nMINESWEEPERS STATISTICS REPORT")
            print(f"-----------------------------------------------------")
            print(f"Beginner Games Played: {bGamesPlayed} | Intermediate Games Played: {iGamesPlayed}")
            print(f"Beginner Games Won: {bGamesWon}    |  Intermediate Games Won: {iGamesWon}")
            print(f"Beginner score: {bPercentWon}%       | Intermediate score: {iPercentWon}%")
            print(f"\nYou won {totalGamesWon} games out of {totalGamesPlayed} games!")
            print(f"\nThat totals to {average}%. That is a {description}")
            
            
        elif selection == "q":
             print("\nThank you for playing Minesweeper!🤖 You quit the game. See you next time!\n")
            
        else:
            print("\nInvalid selection. Please try again.")   

main()
