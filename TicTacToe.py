play = [0, True, False] # [Player, Play_game, player, Repeat_input]
dash = 7 * '-'
empty = 45 * ' '
data = [3 * [0], 3 * [0], 3 * [0]]
view = [3 * [' '], 3 * [' '], 3 * [' ']]
form = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
occupied = 9 * [False]

def player_select (p):
    sign = input ("Please enter 'x' or 'o' to start: ")
    if sign == 'o' or sign == 'O' or sign == '0':
        # player 0 [o, -1]
        p[0] = 0
    else:
        # player 1 [x, +1]
        p[0] = 1
    
def table_print (xlist, ylist):
    print('\n')
    for a in range(5):
        if a % 2 == 1:
            print(dash + '       ' + dash)
        else:
            b = int (a / 2)
            print(f'|{xlist[b][0]}|{xlist[b][1]}|{xlist[b][2]}|       |{ylist[b][0]}|{ylist[b][1]}|{ylist[b][2]}|')   
            
def get_input (p):
    print (empty + "Press 'q' to Quit")
    r = input ('Enter the location number: ')
    if r == 'q' or r == 'Q':
        p [1] = False
        p [2] = False
        return
    if r.isdigit():
        result = int(r) - 1
    else:
        print ('Not a number! Try Again...')
        p [2] = True
        return
    if result >= 0 and result <= 8:
        if occupied [result]:
            print ('Cell already occupied! Try Again...')
            p [2] = True
            return
        occupied [result] = True
        p [2] = False
        r = int (result / 3)
        c = result % 3
        if p [0] == 0:
            # player 0
            data [r][c] = -1
            view [r][c] = 'o'
            # Next Player
            p [0] = 1
            return
        else:
            # player 1
            data [r][c] = 1
            view [r][c] = 'x'
            # Next Player
            p [0] = 0
            return
    else:
        print ('Out of range! Try Again...')
        p [2] = True
        return
    
def check_conditions (d):
    d1 = d[0][0] + d[0][1] + d[0][2] 
    d2 = d[1][0] + d[1][1] + d[1][2] 
    d3 = d[2][0] + d[2][1] + d[2][2] 
    d4 = d[0][0] + d[1][0] + d[2][0] 
    d5 = d[0][1] + d[1][1] + d[2][1] 
    d6 = d[0][2] + d[1][2] + d[2][2] 
    d7 = d[0][0] + d[1][1] + d[2][2]
    d8 = d[0][2] + d[1][1] + d[2][0] 
    
    win = [d1, d2, d3, d4, d5, d6, d7, d8]
    
    if 3 in win:
        # player x wins
        print ("\nPlayer 'x' won the game!")
        play [1] = False
        return 
    elif -3 in win:
        # player 0 wins
        print ("\nPlayer 'o' won the game!")
        play [1] = False
        return 
    return True
    
player_select (play)
while play [1]:
    table_print (view, form)
    get_input (play)
    while play [2]:
        get_input (play)
    play_game = check_conditions (data)
else: 
    table_print (view, form)
    print ('\nGame Over!')