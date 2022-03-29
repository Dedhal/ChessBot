WHITE = 0
BLACK = 1

EIGHT_DIRECTION = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
KNIGHT_DIRECTION = [(2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (-1, -2)]
FOUR_MAIN_DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]
FOUR_DIAG_DIRECTION = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

BISHOP = 0
ROOK = 1
QUEEN = 2

KING = 3
KNIGHT = 4

#--------------------------- Def Pieces Moves -----------------------------#

def Pawn_move(board_state, team, x, y):

    #TODO: Prise en passant

    move = []

    if(team == WHITE):
        #First Move
        if(x == 1 and board_state[x+1][y] == 0 and board_state[x+2][y] == 0):
            move.append((x+2, y))
        #Take
        if(y+1 < 8):
            if(board_state[x+1][y+1]%2 == BLACK):
                move.append((x+1, y+1))
        if(y-1 >= 0):
            if(board_state[x+1][y-1]%2 == BLACK):
                move.append((x+1, y-1))
        #Push
        if(x+1 < 8):
            if(board_state[x+1][y] == 0):
                move.append((x+1, y))

    if(team == BLACK):
        #First Move
        if( x == 6 and board_state[x-1][y] == 0 and board_state[x-2][y] == 0):
            move.append((x-2, y))
        #Take
        if(y+1 < 8):
            if(board_state[x-1][y+1] != 0 and board_state[x-1][y+1]%2 == WHITE):
                move.append((x-1, y+1))
        if(y-1 >= 0):
            if(board_state[x-1][y-1] != 0 and board_state[x-1][y-1]%2 == WHITE):
                move.append((x-1, y-1))
        #Push
        if(x-1 >= 0):
            if(board_state[x-1][y] == 0):
                move.append((x-1, y))

        return (x, y), move

def BRQ_move(board_state, piece, team, x, y):

    move = []

    if(piece == BISHOP):
        loop = FOUR_DIAG_DIRECTION
    elif(piece == ROOK):
        loop = FOUR_MAIN_DIRECTION
    elif(piece == QUEEN):
        loop = EIGHT_MAIN_DIRECTION

    if(team == WHITE):
        ennemy_team = BLACK
    elif(team == BLACK):
        ennemy_team = WHITE

    for index, direction in enumerate(loop):
        for i in range(8):
            if(x+direction[0]*i < 8):
                if(x+direction[0]*i >= 0):
                    if(y+direction[1]*i < 8):
                        if(y+direction[1]*i >= 0):
                            if(board_state[x+direction[0]*i][y+direction[1]*i]%2 == ennemy_team and board_state[x+direction[0]*i][y+direction[1]*i] != 0):
                                move.append((x+direction[0]*i, y+direction[1]*i))
                                break
                            elif(board_state[x+direction[0]*i][y+direction[1]*i] == 0):
                                move.append((x+direction[0]*i, y+direction[1]*i))
                            else:
                                break
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue

    return (x, y), move

def KK_move(board_state, piece, team, x, y):

    move = []

    if(piece == KNIGHT):
        loop = KNIGHT_DIRECTION
    elif(piece == KING):
        loop = KING_DIRECTION

    if(team == WHITE):
        ennemy_team = BLACK
    elif(team == BLACK):
        ennemy_team = WHITE

    for index, direction in enumerate(loop):
        if(x+direction[0] < 8 and x+direction[0] >= 0):
            if(y+direction[1] < 8 and y+direction[1] >=0):
                if(board_state[x+direction[0]][y+direction[1]]%2 == ennemy_team or board_state[x+direction[0]][y+direction[1]] == 0):
                    move.append((x+direction[0], y+direction[1]))

    return (x, y), move

def Actions_List(board_state, team):

    action_list = []

    for i in range(8):
        for x in range(8):
            if(board_state[i][x]!=0 and board_state[i][x]%2==team):
                action_list.append()

    return action_list
