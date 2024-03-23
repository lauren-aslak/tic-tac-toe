import random

board_pos = {
    'A1' : 'empty',
    'A2' : 'empty',
    'A3' : 'empty',
    'B1' : 'empty',
    'B2' : 'empty',
    'B3' : 'empty',
    'C1' : 'empty',
    'C2' : 'empty',
    'C3' : 'empty'
}
coords = {
    'A1' : 1,
    'A2' : 5,
    'A3' : 9,
    'B1' : 1,
    'B2' : 5,
    'B3' : 9,
    'C1' : 1,
    'C2' : 5,
    'C3' : 9
}
coords_list = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
row1 = [' ',' ',' ','||',' ',' ',' ','||',' ',' ',' ',]
row2 = [' ',' ',' ','||',' ',' ',' ','||',' ',' ',' ',]
row3 = [' ',' ',' ','||',' ',' ',' ','||',' ',' ',' ',]
comp_turn = ''
turn_count = 0


def print_board():
    global row1
    global row2
    global row3
    
    print('\n', ''.join(row1), '\n===============\n', ''.join(row2), '\n===============\n', ''.join(row3), '\n')

def user_turn():
    global coords
    global board_pos
    
    print('Your turn')
    while True:
        while True:
            try:
                user_turn = input('Enter desired space: ')
                user_turn = user_turn.upper()
            except KeyError:
                pass
            else:
                if user_turn in board_pos:
                    break
        if board_pos[user_turn] == 'empty':
            if 'A' in user_turn:
                row1[coords[user_turn]] = 'x'
            elif 'B' in user_turn:
                row2[coords[user_turn]] = 'x'
            elif 'C' in user_turn:
                row3[coords[user_turn]] = 'x'
            board_pos[user_turn] = 'x'
            break
        else:
            print('Space already taken.')

def easy_computer_algorithm():
    global comp_turn
    global board_pos
    global coords_list
    global turn_count
    
    #straight accross
    if board_pos['A1'] == 'x' and board_pos['A3'] == 'x' and board_pos['A2'] == 'empty':
        comp_turn = 'A2'
    elif board_pos['B1'] == 'x' and board_pos['B3'] == 'x' and board_pos['B2'] == 'empty':
        comp_turn = 'B2'
    elif board_pos['C1'] == 'x' and board_pos['C3'] == 'x' and board_pos['C2'] == 'empty':
        comp_turn = 'C2'
    #straight down
    elif board_pos['A1'] == 'x' and board_pos['C1'] == 'x' and board_pos['B1'] == 'empty':
        comp_turn = 'B1'
    elif board_pos['A2'] == 'x' and board_pos['C2'] == 'x' and board_pos['B2'] == 'empty':
        comp_turn = 'B2'
    elif board_pos['A3'] == 'x' and board_pos['C3'] == 'x' and board_pos['B3'] == 'empty':
        comp_turn = 'B3'
    #diagnol
    elif board_pos['A1'] == 'x' and board_pos['C3'] == 'x' and board_pos['B2'] == 'empty':
        comp_turn = 'B2'
    elif board_pos['A3'] == 'x' and board_pos['C1'] == 'x' and board_pos['B1'] == 'empty':
        comp_turn = 'B1'
    else:
        comp_turn = random.choice(coords_list)
    turn_count += 1

def medium_computer_algorithm():
    global comp_turn
    global board_pos
    global coords_list
    global turn_count
    
    #straight accross
    #row 1
    if board_pos['A1'] == 'x' and board_pos['A3'] == 'x' and board_pos['A2'] == 'empty':
        comp_turn = 'A2'
    elif board_pos['A1'] == 'x' and board_pos['A2'] == 'x' and board_pos['A3'] == 'empty':
        comp_turn = 'A3'
    elif board_pos['A2'] == 'x' and board_pos['A3'] == 'x' and board_pos['A1'] == 'empty':
        comp_turn = 'A1'
    #row 2
    elif board_pos['B1'] == 'x' and board_pos['B3'] == 'x' and board_pos['B2'] == 'empty':
        comp_turn = 'B2'
    elif board_pos['B1'] == 'x' and board_pos['B2'] == 'x' and board_pos['B3'] == 'empty':
        comp_turn = 'B3'
    elif board_pos['B2'] == 'x' and board_pos['B3'] == 'x' and board_pos['B1'] == 'empty':
        comp_turn = 'B1'
    #row3
    elif board_pos['C1'] == 'x' and board_pos['C3'] == 'x' and board_pos['C2'] == 'empty':
        comp_turn = 'C2'
    elif board_pos['C1'] == 'x' and board_pos['C2'] == 'x' and board_pos['C3'] == 'empty':
        comp_turn = 'C3'
    elif board_pos['C2'] == 'x' and board_pos['C3'] == 'x' and board_pos['C1'] == 'empty':
        comp_turn = 'C1'
    #straight down
    #column 1
    elif board_pos['A1'] == 'x' and board_pos['C1'] == 'x' and board_pos['B1'] == 'empty':
        comp_turn = 'B1'
    elif board_pos['A1'] == 'x' and board_pos['B1'] == 'x' and board_pos['C1'] == 'empty':
        comp_turn = 'C1'
    elif board_pos['B1'] == 'x' and board_pos['C1'] == 'x' and board_pos['A1'] == 'empty':
        comp_turn = 'A1'
    #column 2
    elif board_pos['A2'] == 'x' and board_pos['C2'] == 'x' and board_pos['B2'] == 'empty':
        comp_turn = 'B2'
    elif board_pos['A2'] == 'x' and board_pos['B2'] == 'x' and board_pos['C2'] == 'empty':
        comp_turn = 'C2'
    elif board_pos['B2'] == 'x' and board_pos['C2'] == 'x' and board_pos['A2'] == 'empty':
        comp_turn = 'A2'
    #column 3
    elif board_pos['A3'] == 'x' and board_pos['C3'] == 'x' and board_pos['B3'] == 'empty':
        comp_turn = 'B3'
    elif board_pos['A3'] == 'x' and board_pos['B3'] == 'x' and board_pos['C3'] == 'empty':
        comp_turn = 'C3'
    elif board_pos['B3'] == 'x' and board_pos['C3'] == 'x' and board_pos['A3'] == 'empty':
        comp_turn = 'A3'
    #diagnol
    #starting from top left
    elif board_pos['A1'] == 'x' and board_pos['C3'] == 'x' and board_pos['B2'] == 'empty':
        comp_turn = 'B2'
    elif board_pos['A1'] == 'x' and board_pos['B2'] == 'x' and board_pos['C3'] == 'empty':
        comp_turn = 'C3'
    elif board_pos['C3'] == 'x' and board_pos['B2'] == 'x' and board_pos['A1'] == 'empty':
        comp_turn = 'A1'
    #starting from bottom left
    elif board_pos['A3'] == 'x' and board_pos['C1'] == 'x' and board_pos['B1'] == 'empty':
        comp_turn = 'B1'
    elif board_pos['A3'] == 'x' and board_pos['B2'] == 'x' and board_pos['C1'] == 'empty':
        comp_turn = 'C1'
    elif board_pos['C1'] == 'x' and board_pos['B2'] == 'x' and board_pos['A3'] == 'empty':
        comp_turn = 'A3'
    else:
        comp_turn = random.choice(coords_list)
    turn_count += 1

def difficult_computer_algorithm():
    global comp_turn
    global board_pos
    global coords_list
    global turn_count
    comp_turn = ''
    
    #BLOCKING
    #straight accross
    #row 1
    if board_pos['A1'] == 'x' and board_pos['A3'] == 'x' and board_pos['A2'] == 'empty':
        comp_turn = 'A2'
    elif board_pos['A1'] == 'x' and board_pos['A2'] == 'x' and board_pos['A3'] == 'empty':
        comp_turn = 'A3'
    elif board_pos['A2'] == 'x' and board_pos['A3'] == 'x' and board_pos['A1'] == 'empty':
        comp_turn = 'A1'
    #row 2
    elif board_pos['B1'] == 'x' and board_pos['B3'] == 'x' and board_pos['B2'] == 'empty':
        comp_turn = 'B2'
    elif board_pos['B1'] == 'x' and board_pos['B2'] == 'x' and board_pos['B3'] == 'empty':
        comp_turn = 'B3'
    elif board_pos['B2'] == 'x' and board_pos['B3'] == 'x' and board_pos['B1'] == 'empty':
        comp_turn = 'B1'
    #row3
    elif board_pos['C1'] == 'x' and board_pos['C3'] == 'x' and board_pos['C2'] == 'empty':
        comp_turn = 'C2'
    elif board_pos['C1'] == 'x' and board_pos['C2'] == 'x' and board_pos['C3'] == 'empty':
        comp_turn = 'C3'
    elif board_pos['C2'] == 'x' and board_pos['C3'] == 'x' and board_pos['C1'] == 'empty':
        comp_turn = 'C1'
    #straight down
    #column 1
    elif board_pos['A1'] == 'x' and board_pos['C1'] == 'x' and board_pos['B1'] == 'empty':
        comp_turn = 'B1'
    elif board_pos['A1'] == 'x' and board_pos['B1'] == 'x' and board_pos['C1'] == 'empty':
        comp_turn = 'C1'
    elif board_pos['B1'] == 'x' and board_pos['C1'] == 'x' and board_pos['A1'] == 'empty':
        comp_turn = 'A1'
    #column 2
    elif board_pos['A2'] == 'x' and board_pos['C2'] == 'x' and board_pos['B2'] == 'empty':
        comp_turn = 'B2'
    elif board_pos['A2'] == 'x' and board_pos['B2'] == 'x' and board_pos['C2'] == 'empty':
        comp_turn = 'C2'
    elif board_pos['B2'] == 'x' and board_pos['C2'] == 'x' and board_pos['A2'] == 'empty':
        comp_turn = 'A2'
    #column 3
    elif board_pos['A3'] == 'x' and board_pos['C3'] == 'x' and board_pos['B3'] == 'empty':
        comp_turn = 'B3'
    elif board_pos['A3'] == 'x' and board_pos['B3'] == 'x' and board_pos['C3'] == 'empty':
        comp_turn = 'C3'
    elif board_pos['B3'] == 'x' and board_pos['C3'] == 'x' and board_pos['A3'] == 'empty':
        comp_turn = 'A3'
    #diagnol
    #starting from top left
    elif board_pos['A1'] == 'x' and board_pos['C3'] == 'x' and board_pos['B2'] == 'empty':
        comp_turn = 'B2'
    elif board_pos['A1'] == 'x' and board_pos['B2'] == 'x' and board_pos['C3'] == 'empty':
        comp_turn = 'C3'
    elif board_pos['C3'] == 'x' and board_pos['B2'] == 'x' and board_pos['A1'] == 'empty':
        comp_turn = 'A1'
    #starting from bottom left
    elif board_pos['A3'] == 'x' and board_pos['C1'] == 'x' and board_pos['B1'] == 'empty':
        comp_turn = 'B1'
    elif board_pos['A3'] == 'x' and board_pos['B2'] == 'x' and board_pos['C1'] == 'empty':
        comp_turn = 'C1'
    elif board_pos['C1'] == 'x' and board_pos['B2'] == 'x' and board_pos['A3'] == 'empty':
        comp_turn = 'A3'
    
    
    
    #ATTACKING
    #straight accross
    #row 1
    if board_pos['A1'] == 'o' and board_pos['A3'] == 'o' and board_pos['A2'] == 'empty':
        comp_turn = 'A2'
    elif board_pos['A1'] == 'o' and board_pos['A2'] == 'o' and board_pos['A3'] == 'empty':
        comp_turn = 'A3'
    elif board_pos['A2'] == 'o' and board_pos['A3'] == 'o' and board_pos['A1'] == 'empty':
        comp_turn = 'A1'
    #row 2
    elif board_pos['B1'] == 'o' and board_pos['B3'] == 'o' and board_pos['B2'] == 'empty':
        comp_turn = 'B2'
    elif board_pos['B1'] == 'o' and board_pos['B2'] == 'o' and board_pos['B3'] == 'empty':
        comp_turn = 'B3'
    elif board_pos['B2'] == 'o' and board_pos['B3'] == 'o' and board_pos['B1'] == 'empty':
        comp_turn = 'B1'
    #row3
    elif board_pos['C1'] == 'o' and board_pos['C3'] == 'o' and board_pos['C2'] == 'empty':
        comp_turn = 'C2'
    elif board_pos['C1'] == 'o' and board_pos['C2'] == 'o' and board_pos['C3'] == 'empty':
        comp_turn = 'C3'
    elif board_pos['C2'] == 'o' and board_pos['C3'] == 'o' and board_pos['C1'] == 'empty':
        comp_turn = 'C1'
    #straight down
    #column 1
    elif board_pos['A1'] == 'o' and board_pos['C1'] == 'o' and board_pos['B1'] == 'empty':
        comp_turn = 'B1'
    elif board_pos['A1'] == 'o' and board_pos['B1'] == 'o' and board_pos['C1'] == 'empty':
        comp_turn = 'C1'
    elif board_pos['B1'] == 'o' and board_pos['C1'] == 'o' and board_pos['A1'] == 'empty':
        comp_turn = 'A1'
    #column 2
    elif board_pos['A2'] == 'o' and board_pos['C2'] == 'o' and board_pos['B2'] == 'empty':
        comp_turn = 'B2'
    elif board_pos['A2'] == 'o' and board_pos['B2'] == 'o' and board_pos['C2'] == 'empty':
        comp_turn = 'C2'
    elif board_pos['B2'] == 'o' and board_pos['C2'] == 'o' and board_pos['A2'] == 'empty':
        comp_turn = 'A2'
    #column 3
    elif board_pos['A3'] == 'o' and board_pos['C3'] == 'o' and board_pos['B3'] == 'empty':
        comp_turn = 'B3'
    elif board_pos['A3'] == 'o' and board_pos['B3'] == 'o' and board_pos['C3'] == 'empty':
        comp_turn = 'C3'
    elif board_pos['B3'] == 'o' and board_pos['C3'] == 'o' and board_pos['A3'] == 'empty':
        comp_turn = 'A3'
    #diagnol
    #starting from top left
    elif board_pos['A1'] == 'o' and board_pos['C3'] == 'o' and board_pos['B2'] == 'empty':
        comp_turn = 'B2'
    elif board_pos['A1'] == 'o' and board_pos['B2'] == 'o' and board_pos['C3'] == 'empty':
        comp_turn = 'C3'
    elif board_pos['C3'] == 'o' and board_pos['B2'] == 'o' and board_pos['A1'] == 'empty':
        comp_turn = 'A1'
    #starting from bottom left
    elif board_pos['A3'] == 'o' and board_pos['C1'] == 'o' and board_pos['B1'] == 'empty':
        comp_turn = 'B1'
    elif board_pos['A3'] == 'o' and board_pos['B2'] == 'o' and board_pos['C1'] == 'empty':
        comp_turn = 'C1'
    elif board_pos['C1'] == 'o' and board_pos['B2'] == 'o' and board_pos['A3'] == 'empty':
        comp_turn = 'A3'
    elif comp_turn == '':
        comp_turn = random.choice(coords_list)
    turn_count += 1

def computer_turn():
    global coords
    global board_pos
    global comp_turn
    global difficulty
    
    print("Computer's turn")
    while True:
        if difficulty.lower() == 'hard':
            difficult_computer_algorithm()
        elif difficulty.lower() == 'medium':
            medium_computer_algorithm()
        elif difficulty.lower() == 'easy':
            easy_computer_algorithm()
        
        if board_pos[comp_turn] == 'empty':
            if 'A' in comp_turn:
                row1[coords[comp_turn]] = 'o'
            elif 'B' in comp_turn:
                row2[coords[comp_turn]] = 'o'
            elif 'C' in comp_turn:
                row3[coords[comp_turn]] = 'o'
            board_pos[comp_turn] = 'o'
            break

def reset():
    global board_pos
    global row1
    global row2
    global row3
    
    board_pos = {
        'A1' : 'empty',
        'A2' : 'empty',
        'A3' : 'empty',
        'B1' : 'empty',
        'B2' : 'empty',
        'B3' : 'empty',
        'C1' : 'empty',
        'C2' : 'empty',
        'C3' : 'empty'
    }
    row1 = [' ',' ',' ','||',' ',' ',' ','||',' ',' ',' ',]
    row2 = [' ',' ',' ','||',' ',' ',' ','||',' ',' ',' ',]
    row3 = [' ',' ',' ','||',' ',' ',' ','||',' ',' ',' ',]


def main():
    global coords
    global board_pos
    global turn_count
    
    while True:
        reset()
        while True:
            print_board()
            flow_control = input('(press enter to continue)')
            
            if board_pos['A1'] == 'o' and board_pos['B1'] == 'o' and board_pos['C1'] == 'o':
                print('You lose, computer wins!')
                break
            elif board_pos['A1'] == 'o' and board_pos['B2'] == 'o' and board_pos['C3'] == 'o':
                print('You lose, computer wins!')
                break
            elif board_pos['A1'] == 'o' and board_pos['A2'] == 'o' and board_pos['A3'] == 'o':
                print('You lose, computer wins!')
                break
            elif board_pos['B1'] == 'o' and board_pos['B2'] == 'o' and board_pos['B3'] == 'o':
                print('You lose, computer wins!')
                break
            elif board_pos['C1'] == 'o' and board_pos['C2'] == 'o' and board_pos['C3'] == 'o':
                print('You lose, computer wins!')
                break
            elif board_pos['A3'] == 'o' and board_pos['B2'] == 'o' and board_pos['C1'] == 'o':
                print('You lose, computer wins!')
                break
            elif board_pos['A2'] == 'o' and board_pos['B2'] == 'o' and board_pos['C2'] == 'o':
                print('You win!')
                break
            elif turn_count >= 6:
                print('Tie!')
                break
            
            user_turn()
            print_board()
            
            if board_pos['A1'] == 'x' and board_pos['B1'] == 'x' and board_pos['C1'] == 'x':
                print_board()
                print('You win!')
                break
            elif board_pos['A1'] == 'x' and board_pos['B2'] == 'x' and board_pos['C3'] == 'x':
                print_board()
                print('You win!')
                break
            elif board_pos['A1'] == 'x' and board_pos['A2'] == 'x' and board_pos['A3'] == 'x':
                print_board()
                print('You win!')
                break
            elif board_pos['B1'] == 'x' and board_pos['B2'] == 'x' and board_pos['B3'] == 'x':
                print_board()
                print('You win!')
                break
            elif board_pos['C1'] == 'x' and board_pos['C2'] == 'x' and board_pos['C3'] == 'x':
                print_board()
                print('You win!')
                break
            elif board_pos['A3'] == 'x' and board_pos['B2'] == 'x' and board_pos['C1'] == 'x':
                print_board()
                print('You win!')
                break
            elif board_pos['A2'] == 'x' and board_pos['B2'] == 'x' and board_pos['C2'] == 'x':
                print_board()
                print('You win!')
                break
            
            computer_turn()
        restart = input('Play again?(Y/N) ')
        if restart.upper() == 'N':
            break
        else:
            while True:
                turn_count = 0
                difficulty = input('What difficulty would you like to play at: easy, medium, hard? ')
                if difficulty.lower() != 'easy' and difficulty.lower() != 'medium' and difficulty.lower() != 'hard':
                    print('Invalid input. Please enter easy, medium, or hard.')
                else:
                    break














print('~~~Welcome to Tic Tac Toe~~~\n\nHere is the board')
print('   1    2    3\nA   ||   ||\n===============\nB   ||   ||\n===============\nC   ||   ||\n\n')
while True:
    difficulty = input('What difficulty would you like to play at: easy, medium, hard? ')
    if difficulty.lower() != 'easy' and difficulty.lower() != 'medium' and difficulty.lower() != 'hard':
        print('Invalid input. Please enter easy, medium, or hard.')
    else:
        break
main()
