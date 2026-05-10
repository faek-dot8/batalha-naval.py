#batalha naval
import random
shoots = 0
ships = 5
hiden_ships = [["~" for _ in range(5)]for _ in range(5)]
board = [["~" for _ in range(5)] for _ in range(5)]

#gerating ships
while True:
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    if hiden_ships[x][y] == "~":
        hiden_ships[x][y] = "X"
        hiden_ships[x][y] = "X"
        ships -= 1
    if ships == 0:
        break

ships = 5
  #game loop
while True:  
    for i in range(5):
        print(" ".join(board[i]))
    line = int(input("Enter the line (0-4): "))
    column = int(input("Enter the column (0-4): "))
    shoots += 1
    if not (0 <= line < 5 and 0 <= column < 5):
        print("Please enter coordinates within the board.")
        continue
    if hiden_ships[line][column] == "X":
        print("Hit!")
        board[line][column] = "X"
        hiden_ships[line][column] = "~"
        ships -= 1
    else:
        print("Miss!")
        board[line][column] = "O"
    
    if ships == 0:
        print(f"Congratulations! You sank all the ships in {shoots} shots.")
        break
    if shoots == 10:
        print("Game over! You've used all your shots.")
        break