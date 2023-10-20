board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ',]

def _display(b):
    print(f'{b[0]}|{b[1]}|{b[2]}')
    print('-----')
    print(f'{b[3]}|{b[4]}|{b[5]}')
    print('-----')
    print(f'{b[6]}|{b[7]}|{b[8]}')

def _chooseplayer():
    result = ''
    approved = False
    while(not approved):
        result = input("Player 1 please choose 'X' or 'O':")
        if(result == 'X' or result == 'O'):
            approved = True
    
    return result

def _playerturn(p):
    return ("Player1's turn!" if p else "Player2's turn!")

def _wincheck(mark, location):

    global board
    board[location] = mark
    _display(board)
    
    for x in range(0,len(board),3):
        if board[x] == board [x+1] == board[x+2] == mark:
            print(f"{mark} wins!")
            return True
    if board[0] == board [4] == board[8] == mark:
            print(f"{mark} wins!")
            return True
    if board[2] == board [4] == board[6] == mark:
            print(f"{mark} wins!")
            return True
    for x in range(3):
        if board[x] == board[x+3] == board[x+6] == mark:
            print(f"{mark} wins!")
            return True
        
    if board.count(' ') == 0:
        print("It's a tie!")
        return True

    return False

def _userinput():
    valid = False
    action = ''
    
    while not valid:
        action = input("Please enter a location between from 0 to 8:")
        if(action.isdigit()):
             action = int(action)
             if 0<= action <=8:
                  valid = True
    
    return action

def _gameplay():
    ongoing = True
    p1t, p2t = True, False

    player1 = _chooseplayer()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    while ongoing:
        location = _userinput()
        if(board[location] != ' '):
            print("Location already occupied, Try again!")
            continue
        if(p1t):
            if(_wincheck(player1,location)):
                ongoing = False
            p1t = False
        else:
            if(_wincheck(player2, location)):
                ongoing = False
            p1t = True

_gameplay()

