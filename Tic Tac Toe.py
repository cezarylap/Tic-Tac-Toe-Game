import random

win_space = {1:[1,2,3], 2:[4,5,6], 3:[7,8,9],
             4:[1,4,7], 5:[2,5,8], 6:[3,6,9],
             7:[1,5,9], 8:[3,5,7]}

best_moves = {1:5, 2:1, 3:3, 4:7, 5:9, 6:2, 7:4, 8:6, 9:8}

def start():
    global play_space, player_order, turn, move, human_move_list, computer_move_list, board_place
    print("Welcome in Tic Tac Toe game")
    print("This is how the fields are positioned on the board:")
    print("""
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
    """)
    play_space = [1,2,3,4,5,6,7,8,9]
    turn = 1
    move = None
    human_move_list = []
    computer_move_list = []
    board_place ={}
    for x in range(1,10, 1):
        board_place.update({x:" "})  
    player_order = random.randint(0, 1)
    if player_order == 0:
        print("Your turn")
    else:
        print("CPU turn")

def board():
    print(" ", board_place[1], "|", board_place[2], "|", board_place[3], "\n"
      "  ---------\n"
      " ", board_place[4], "|", board_place[5], "|", board_place[6], "\n"
      "  ---------\n"
      " ", board_place[7], "|", board_place[8], "|", board_place[9], "\n")    

def whos_moving(): #Returns 0 if it is human turn and 1 if CPU turn
    if player_order == 0:
        if turn % 2 == 1:
            return 0
        else:
            return 1
    else:
        if turn % 2 == 1:
            return 1
        else:
            return 0

def token():
    global turn
    if turn % 2 == 0:
        return "O"
    else:
        return "X"

def human_move():
    global move
    move = None 
    while move not in play_space:
        move = int(input("Which field do you choose? "))
        if move not in play_space:
            print("Unauthorized field")
    print("You have selected the field: ", move)
    human_move_list.append(move)

#CPU logic
def computer_move():
    global move, computer_move_list
    move = None
    #see if there is a move available that will allow you to win
    for element in play_space:
        computer_move_list_copy = computer_move_list.copy()
        computer_move_list_copy.append(element)
        answer = win(human_move_list, computer_move_list_copy)
        if answer == 1:
            move = element
            break
        computer_move_list_copy.remove(element)
    #if no computer move wins check if the human doesn't win in the next round
    if move == None:
        for element in play_space:
            human_move_list_copy = human_move_list.copy()
            human_move_list_copy.append(element)
            answer = win(human_move_list_copy, computer_move_list)
            if answer == 0:
                move = element
                break
            human_move_list_copy.remove(element)          
    #moves from best to worst
    if move == None:
        for element in best_moves:
            if best_moves[element] in play_space:
                move = best_moves[element]
                break
    print("The computer selected the field: ", move)
    computer_move_list.append(move)

def board_update():
    global move
    play_space.remove(move)
    board_place[move] = token()
    board()

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

#Checking if someone has won
def win(human_moves, computer_moves):
    global turn
    for element in win_space:
        h = intersection(win_space[element], human_moves)
        c = intersection(win_space[element], computer_moves)
        if len(h) == 3:
            print("Congratulations you beat the computer")
            return 0
            break
        elif len(c) == 3:
            print("The computer won the skirmish")
            return 1
            break
        elif turn == 9:
            print("Draw")
            break
    return 2 #when there is no winner or draw

def main():
    global turn
    start()
    for turn in range(1, 10, 1):
        if whos_moving() == 0:
            human_move()
        else:
            computer_move()
        board_update()
        if win(human_move_list, computer_move_list) in [0,1]:
            break
    restart = input("Do you want to play again? yes/no: ")
    if restart == "yes":
        main()
    else:
        print("End game")

main()