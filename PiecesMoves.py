WHITE = 0
BLACK = 1

EIGHT_DIRECTION = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
KNIGHT_DIRECTION = [(2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (-1, -2)]
FOUR_MAIN_DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]
FOUR_DIAG_DIRECTION = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

W_PAWN_VALUE = 2
W_KNIGHT_VALUE = 4
W_BISHOP_VALUE = 6
W_ROOK_VALUE = 8
W_QUEEN_VALUE = 10
W_KING_VALUE = 12

B_PAWN_VALUE = 1
B_KNIGHT_VALUE = 3
B_BISHOP_VALUE = 5
B_ROOK_VALUE = 7
B_QUEEN_VALUE = 9
B_KING_VALUE = 11

BRQ = 0
KK = 1
PAWN = 2

#--------------------------- Def Pieces Moves -----------------------------#

def Piece_move(board_state, team, x, y):

    move = []

    if(board_state[x][y]==W_BISHOP_VALUE or board_state[x][y]==B_BISHOP_VALUE):
        loop = FOUR_DIAG_DIRECTION
        movement_type = BRQ
    elif(board_state[x][y]==W_ROOK_VALUE or board_state[x][y]==B_ROOK_VALUE):
        loop = FOUR_MAIN_DIRECTION
        movement_type = BRQ
    elif(board_state[x][y]==W_QUEEN_VALUE or board_state[x][y]==B_QUEEN_VALUE):
        loop = EIGHT_DIRECTION
        movement_type = BRQ
    elif(board_state[x][y]==W_KNIGHT_VALUE or board_state[x][y]==B_KNIGHT_VALUE):
        loop = KNIGHT_DIRECTION
        movement_type = KK
    elif(board_state[x][y]==W_KING_VALUE or board_state[x][y]==B_KING_VALUE):
        loop = EIGHT_DIRECTION
        movement_type = KK
    else:
        movement_type = PAWN

    if(team == WHITE):
        ennemy_team = BLACK
    elif(team == BLACK):
        ennemy_team = WHITE

    if(movement_type == BRQ):
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

    elif(movement_type == KK):
        for index, direction in enumerate(loop):
            if(x+direction[0] < 8 and x+direction[0] >= 0):
                if(y+direction[1] < 8 and y+direction[1] >=0):
                    if(board_state[x+direction[0]][y+direction[1]]%2 == ennemy_team or board_state[x+direction[0]][y+direction[1]] == 0):
                        move.append((x+direction[0], y+direction[1]))

    elif(movement_type == PAWN):
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

def Actions_List(board_state, team):

    action_list = []

    for i in range(8):
        for x in range(8):
            if(board_state[i][x]!=0 and board_state[i][x]%2==team):
                action_list.append()

    return action_list
