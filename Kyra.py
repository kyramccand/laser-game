#Kyra.py
import random

def main():
    num_lasers_shot = 0
    num_mirrors_found = 0
    print("\n ============================================\n\n          Welcome to the Laser Game!\n\n ============================================")
    game_board = create_board()
    display(game_board)
    
    while num_mirrors_found < 10 and num_mirrors_found != -1:
        num_lasers_shot, num_mirrors_found =  menu(game_board, num_lasers_shot, num_mirrors_found)

    if num_mirrors_found == 10:
        print("\nCongratulations! You won!")
    print("\nThanks for playing!")
    
def menu(this_board, num_shot, num_found):
    choice = ""
    print("\n                    Menu\n\n  1. Shoot a laser\n  2. Guess a mirror location\n  0. Quit\n")
    while choice != "0" and choice != "1" and choice != "2" and choice != "3":
        choice = input("  Choose an option: ")
    choice = int(choice)
    if choice == 0:
        return num_shot, -1
    if choice == 1:
        num_shot += 1
        display(this_board)
        laser = input("Which laser?: ")
        print("The beam emerged at laser #" + str(shoot_laser(int(laser), this_board)) + ".")
        display_stats(num_shot, num_found)
    elif choice == 2:
        display(this_board)
        top_coord = int(input("Enter the top coordinate: "))
        right_coord = int(input("Enter the right coordinate: "))
        num_found = guess_mirror(top_coord, right_coord, this_board, num_found)
        display_stats(num_shot, num_found)
    elif choice == 3:
        cheat_display(this_board)
    
    return num_shot, num_found
        
        
    
def create_board():
    board = []
    for i in range(10):
        board.append([])
        for j in range(10):
            board[i].append(".")
    
    mirror_count = 0
    while mirror_count < 10:
        r = random.randint(0, 9)
        c = random.randint(0, 9)
        if board[r][c] == ".":
            board[r][c] = "0"
            if random.random() < 0.5:
                board[r][c] = "1"
            mirror_count += 1
            
    return board

def cheat_display(this_board):
    print("\n                  Game Board\n\n     0   1   2   3   4   5   6   7   8   9\n")
    for r in range(len(this_board)):
        row = str(39 - r) + " "
        for c in range(len(this_board[r])):
            if this_board[r][c] == "1":
                 row += "  / "
            elif this_board[r][c] == "0":
                row += "  \\ "
            else:
                row += "  " + this_board[r][c] + " "
        print(row + " " + str(10 + r) + "\n")
    print("     29  28  27  26  25  24  23  22  21  20\n")

def display(this_board):
    print("\n                  Game Board\n\n     0   1   2   3   4   5   6   7   8   9\n")
    for r in range(len(this_board)):
        row = str(39 - r) + " "
        for c in range(len(this_board[r])):
            if this_board[r][c] == "1" or this_board[r][c] == "0":
                row += "  . "
            else:
                row += "  " + this_board[r][c] + " "
        print(row + " " + str(10 + r) + "\n")
    print("     29  28  27  26  25  24  23  22  21  20\n")

def display_stats(num_shot, num_found):
    print("\n                  Game Stats \n\n       You have found " + str(num_found) + " out of 10 mirrors.\n             You have shot " + str(num_shot) + " lasers.")

def guess_mirror_helper(x, y, this_board, num_found):
    if x >= 0 and x <= 9 and y >= 10 and y <= 19:
        if this_board[y - 10][x] == "1" or this_board[y - 10][x] == "0":
            print("You found a mirror!")
            num_found += 1
            return True
        print("No luck...")
        return False

def guess_mirror(x, y, this_board, num_found):
    if guess_mirror_helper(x, y, this_board, num_found):
        num_found += 1
        if this_board[y - 10][x] == "1":
            this_board[y - 10][x] = "/"
        elif this_board[y - 10][x] == "0":
            this_board[y - 10][x] = "\\"
        display(this_board)
    return num_found

def shoot_laser(laser_num, this_board):
    direction = ">"
    x = 0
    y = 39 - laser_num
    if laser_num < 10:
        direction = "v"
        x = laser_num
        y = 0
    elif laser_num < 20:
        x = 9
        y = laser_num - 10
        direction = "<"
    elif laser_num < 30:
        x = 29 - laser_num
        y = 9
        direction = "^"
    return shoot_laser_helper(x, y, direction, this_board)

def shoot_laser_helper(x, y, dir, this_board):
    dir = update_direction(x, y, dir, this_board)
    if dir == "^":
        y -= 1
    elif dir == ">":
        x += 1
    elif dir == "v":
        y += 1
    elif dir == "<":
        x -= 1
        
    if x < 0:
        return 39 - y
    elif x > 9:
        return 10 + y
    elif y < 0:
        return x
    elif y > 9:
        return 29 - x
    else:
        return shoot_laser_helper(x, y, dir, this_board)

def update_direction(x, y, dir, this_board):
    if this_board[y][x] == "/" or this_board[y][x] == "1":
        if dir == "^":
            dir = ">"
        elif dir == ">":
            dir = "^"
        elif dir == "v":
            dir = "<"
        elif dir == "<":
            dir = "v"
    elif this_board[y][x] == "\\" or this_board[y][x] == "0":
        if dir == "^":
            dir = "<"
        elif dir == "<":
            dir = "^"
        elif dir == "v":
            dir = ">"
        elif dir == ">":
            dir = "v"
    return dir

main()
