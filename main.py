# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# NEEDS
# Make a case for stalemates using the counter as an indicator

# Initializes storage for Game
while True:

    grid = list()
    turn_statement = "Player %s what position would you like to play in?"
    win_statement = "Congratulations Player %s! You win!"
    for i in range(10):
        grid.append(str(i))
    game = ""
    counter = 1
    grid_pick = -1
    resetInput = ''
    while game != "over":
        game = "active"
        oddPlayer = "X"
        evenPlayer = "O"
        turn = ""
        # basic turn pick, & display
        if counter % 2 == 0:
            turn = evenPlayer
        else:
            turn = oddPlayer
        print(turn_statement%(turn))

        for i in range(1, 10, 3):
            print(grid[i], grid[i + 1], grid[i + 2])

        while grid_pick not in grid or grid_pick == "0":
            grid_pick = input("Select a number shown above to place your letter: ")
        grid[int(grid_pick)] = turn
        # Win checker
        for i in range(1, 10, 3):
            if grid[i] == grid[i+1] == grid[i+2]:
                print(win_statement%(turn))
                for i in range(1, 10, 3):
                    print(grid[i], grid[i + 1], grid[i + 2])
                game = "over"
        for i in range(1, 4):
            if grid[i] == grid[i+3] == grid[i+6]:
                print(win_statement%(turn))
                for i in range(1, 10, 3):
                    print(grid[i], grid[i + 1], grid[i + 2])
                game = "over"
        if grid[1] == grid[5] == grid[9] or grid[3] == grid[5] == grid[7]:
            print(win_statement % (turn))
            for i in range(1, 10, 3):
                print(grid[i], grid[i + 1], grid[i + 2])
            game = "over"
        counter += 1
        if counter == 10 and game != 'over':
            print("Cat's Game!")
            for i in range(1, 10, 3):
                print(grid[i], grid[i + 1], grid[i + 2])
            game = 'over'

        print("")

    # reset test
    while resetInput != "Y" and resetInput != "N":
        resetInput = input("Would you like to play again? Please input a Y or N. ")
    if resetInput == "Y":
        continue;
    else:
        print("Goodbye")
        break
