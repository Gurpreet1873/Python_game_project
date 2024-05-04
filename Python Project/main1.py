# variables for tic Tac Toe
currentPlayer = "X"
winner = None
gameRunning = True


playerOnline = True

def ticTacToe():
    board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']

    #printing board

    def printBoard(board):
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("-" * 9)
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("-" * 9)
        print(board[6] + " | " + board[7] + " | " + board[8])

    #take player input
    def playerInput(board):
        while True:
            if currentPlayer == "X":
                inp = int(input(f"Enter a number 1-9 \033[1;34m Player (X) \033[0;0m : "))
            else:
                inp = int(input(f"Enter a number 1-9 \033[1;31m Player (0) \033[0;0m : "))
            if inp >= 1 and inp <= 9 and board[inp-1] == "-":
                board[inp-1] = currentPlayer
                break
            else:
                if currentPlayer == "X":
                    print(f"Oops! Try again! Player - \033[1;34m Player (X) \033[0;0m ! ")
                else:
                    print(f"Oops! Try again! Player - \033[1;31m Player (0) \033[0;0m ! ")
                printBoard(board)


    #check for win or tie
    def checkHorizontal(board):
        global winner
        if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
            winner = currentPlayer
            return True
    def checkRow(board):
        global winner
        if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] != "-"):
            winner = currentPlayer
            return True
    def checkDiagonal(board):
        global winner
        if (board[0] == board[4] == board[5] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
            winner = currentPlayer
            return True
    def checkTie(board):
        global gameRunning
        if "-" not in board:
            printBoard(board)
            print("Its a tie")
            gameRunning = False

    def checkWin():
        if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
            print(f"The winner is {winner}")

    #switch the player
    def switchPlayer():
        global currentPlayer
        if currentPlayer == "X":
            currentPlayer = "O"
        else:
            currentPlayer = "X"



    #check for win or tie again

    while gameRunning:
        printBoard(board)
        if winner != None:
            break
        playerInput(board)
        checkWin()
        checkTie(board)
        switchPlayer()

def numberGuessingGame():
    import random

    secretNumber = random.randint(1, 100)
    
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    while True:
        guess = input("Enter your guess (or 'q' to quit): ")
        
        if guess.lower() == 'q':
            print("Thanks for playing! The number was", secretNumber)
            break
        
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        
        attempts += 1
        
        if guess == secretNumber:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            break
        elif guess < secretNumber:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

def rockPaperScissors():
    import random
    options = ['rock', 'paper', 'scissors']
    
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        playerChoice = input("Enter your choice (rock, paper, or scissors): ").lower()
        
        if playerChoice not in options:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue
        
        computerChoice = random.choice(options)
        
        print("You chose:", playerChoice)
        print("Computer chose:", computerChoice)
        
        if playerChoice == computerChoice:
            print("It's a tie!")
        elif (playerChoice == 'rock' and computerChoice == 'scissors') or \
             (playerChoice == 'paper' and computerChoice == 'rock') or \
             (playerChoice == 'scissors' and computerChoice == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")
        
        playAgain = input("Do you want to play again? (yes/no): ").lower()
        if playAgain != 'yes':
            print("Thanks for playing!")
            break

def marioGame():
    pass

while playerOnline:
    print("Welcome to Fun Zone !!!")
    wantToPlay = input("You want to play the game yes/no ").lower()
    if wantToPlay == "no":
        playerOnline = False 
        break

    paidOrNot  = input("Are you a premium user yes/no ").lower()
    
    if paidOrNot == "yes":
        marioGame()
    else:
        nonPremiumGameChoice = int(input("Enter the game you want to play 1 for ticTacToe , 2 for numberGuessingGame , 3 for rockPaperScissor "))
        if nonPremiumGameChoice == 1:
            ticTacToe()
        elif nonPremiumGameChoice == 2:
            numberGuessingGame()
        elif nonPremiumGameChoice == 3:
            rockPaperScissors()
