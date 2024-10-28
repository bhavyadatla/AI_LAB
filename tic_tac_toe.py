import random

def generateMagicSquare():
    magicSquare = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ]
    return magicSquare

def printMagicSquareWithMoves(magicSquare, player_moves, computer_moves, player_symbol, computer_symbol):
    print("Magic Square:")
    for row in magicSquare:
        print(' | '.join(
            f'{player_symbol}' if num in player_moves else
            f'{computer_symbol}' if num in computer_moves else
            f'{num:1}'                          
            for num in row
        ))
        print('-' * 9)

def checkWin(magicSquare, n, moves):
    magic_constant = n * (n * n + 1) // 2
    for i in range(n):
        if sum(magicSquare[i][j] for j in range(n) if magicSquare[i][j] in moves) == magic_constant:
            return True
        if sum(magicSquare[j][i] for j in range(n) if magicSquare[j][i] in moves) == magic_constant:
            return True
    if sum(magicSquare[i][i] for i in range(n) if magicSquare[i][i] in moves) == magic_constant:
        return True
    if sum(magicSquare[i][n - i - 1] for i in range(n) if magicSquare[i][n - i - 1] in moves) == magic_constant:
        return True
    return False

def findWinningMove(magicSquare, n, moves, available_numbers):
    for number in available_numbers:
        temp_moves = moves + [number]
        if checkWin(magicSquare, n, temp_moves):
            return number
    return None

def tossForFirstPlayer():
    ch = random.choice([0, 1])
    print('Toss result: ', ch)
    return ch

def playGame(magicSquare, n):
    available_numbers = [num for row in magicSquare for num in row]
    player_moves = []
    computer_moves = []
    printMagicSquareWithMoves(magicSquare, player_moves, computer_moves, " ", " ")

    while True:
        try:
            human_choice = input('Select a number "0" or "1" for the toss: ')
            if human_choice in ["0", "1"]:
                human_choice = int(human_choice)
                break
            else:
                print("Enter a valid input! Only 0 or 1 is allowed.")
        except ValueError:
            print("Enter a valid input!")

    toss_result = tossForFirstPlayer()
    if human_choice == toss_result:
        print("Human won the toss!!")
        player_symbol = 'X'
        computer_symbol = 'O'
        current_player = 'X'
    else:
        print("Computer won the toss!!")
        player_symbol = 'O'
        computer_symbol = 'X'
        current_player = 'X'

    for turn in range(n * n):
        if current_player == 'X':
            if computer_symbol == 'X':
                winning_move = findWinningMove(magicSquare, n, computer_moves, available_numbers)
                if winning_move is not None:
                    computer_move = winning_move
                else:
                    blocking_move = findWinningMove(magicSquare, n, player_moves, available_numbers)
                    if blocking_move is not None:
                        computer_move = blocking_move
                    else:
                        computer_move = random.choice(available_numbers)
                print(f"Computer's choice: {computer_move}")
                computer_moves.append(computer_move)
                available_numbers.remove(computer_move)
            else:
                while True:
                    try:
                        player_move = int(input(f"Select number from the board: "))
                        if player_move not in available_numbers:
                            raise ValueError("Invalid choice. Choose from the available numbers.")
                        if player_move <= 0:  # Check for negative values and zero
                            raise ValueError("Negative values and zero are not allowed.")
                        break
                    except ValueError:
                        print("Enter a valid input!")
                player_moves.append(player_move)
                available_numbers.remove(player_move)
            current_player = 'O'
        else:
            if player_symbol == 'O':
                while True:
                    try:
                        player_move = int(input(f"Select number from the board: "))
                        if player_move not in available_numbers:
                            raise ValueError("Invalid choice. Choose from the available numbers.")
                        if player_move <= 0:  # Check for negative values and zero
                            raise ValueError("Negative values and zero are not allowed.")
                        break
                    except ValueError:
                        print("Enter a valid input!")
                player_moves.append(player_move)
                available_numbers.remove(player_move)
            else:
                winning_move = findWinningMove(magicSquare, n, computer_moves, available_numbers)
                if winning_move is not None:
                    computer_move = winning_move
                else:
                    blocking_move = findWinningMove(magicSquare, n, player_moves, available_numbers)
                    if blocking_move is not None:
                        computer_move = blocking_move
                    else:
                        computer_move = random.choice(available_numbers)
                print(f"Computer's choice: {computer_move}")
                computer_moves.append(computer_move)
                available_numbers.remove(computer_move)
            current_player = 'X'

        printMagicSquareWithMoves(magicSquare, player_moves, computer_moves, player_symbol, computer_symbol)
        if checkWin(magicSquare, n, computer_moves):
            print("Computer wins!")
            return
        elif checkWin(magicSquare, n, player_moves):
            print("Player wins!")
            return

    print("It's a draw!")

def main():
    while True:
        magicSquare = generateMagicSquare()
        playGame(magicSquare, 3)
        while True:
            play_again = input("Would you like to play again? (yes/no): ").lower()
            if play_again in ['yes']:
                break  
            elif play_again in ['no']:
                print("Thanks for playing!")
                return
            else:
                print("Please enter 'yes' for yes or 'no' for no.")

main()
