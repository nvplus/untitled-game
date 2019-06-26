grid = [
    [0, 0, 0, 0],
    [0, 2, 2, 0],
    [0, 2, 2, 0],
    [0, 1, 0, 0]
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
    return False

def update_board(old_pos, new_pos):
    grid[old_pos[1] - 1][old_pos[1] - 1] = 0 
    grid[new_pos[1] - 1][new_pos[1] - 1] = 1 

def do_movement(player_input, grid):
    pos = read_position(grid)
    new_pos = pos.copy()

    if player_input is "x":
        raise Exception("Done")

    elif player_input is "l":
        new_pos[0] -= 1
        print(new_pos)

    elif player_input is "d":
        new_pos[0][0] += 1

    elif player_input is "u":
        new_pos[0] -= 1

    elif player_input is "r":
        new_pos[0][0] += 1

    print("Move: " + str(pos) + " -> " + str(new_pos))

    if not check_collision(new_pos):
        update_board(pos, new_pos)
    
    return

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

    do_movement(player_input, grid)
