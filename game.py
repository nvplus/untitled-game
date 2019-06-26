grid = [
    [0, 0, 0, 0],
    [0, 2, 2, 0],
    [0, 2, 2, 0],
    [0, 0, 1, 0]
]

def read_position(grid):
    y = 1
    for row in grid:
        for x in range(len(row)):
            if row[x] is 1:
                return [x+1, y]
        y += 1

    return [-1, -1]

def check_collision(position):
    """
    Returns True if player has collided with a wall or has gone out of bounds
    """
    try:
        grid[position[1] - 1][position[0] - 1]
    except:
        print("DEBUG: Out of bounds detected.")
        return True

    print("DEBUG: Collision detected.")
    return grid[position[1] - 1][position[0] - 1] is not 0

def update_board(old_pos, new_pos):
    grid[old_pos[1] - 1][old_pos[0] - 1] = 0
    grid[new_pos[1] - 1][new_pos[0] - 1] = 1 

def do_movement(player_input, grid):
    pos = read_position(grid)
    new_pos = pos.copy()

    if player_input is "l":
        new_pos[0] -= 1

    elif player_input is "d":
        new_pos = [new_pos[0], new_pos[1] + 1]

    elif player_input is "u":
        new_pos = [new_pos[0], new_pos[1] - 1]

    elif player_input is "r":
        new_pos[0] += 1

    if not check_collision(new_pos):
        update_board(pos, new_pos)

def convert_to_game_char(value):
    if value is 0:
        return "-"
    elif value is 1:
        return "O"
    else:
        return "X"

def draw_grid(grid):
    for row in grid:
        print("| ", end = "")
        for column in row:
            print(convert_to_game_char(column), end = " ")
        print("|", end = "\n")

#Main loop

done = False

while not done:
    draw_grid(grid)

    player_input = input("Enter an input: ")

    if player_input == "exit":
        print("\nThank you for playing!")
        done = True

    else:
        do_movement(player_input, grid)

        print()
