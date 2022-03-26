WHITE = 0
BLACK = 1

#--------------------------- Def Pieces Moves -----------------------------#

def Pawn_move(board_state, team, x, y):

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

def Knight_move(board_state, team, x, y):

    move = []

    if(team == WHITE):
        if(x+2 < 8):
            if(y+1 < 8):
                if(board_state[x+2][y+1]%2 == BLACK or board_state[x+2][y+1] == 0):
                    move.append((x+2, y+1))
        if(x+2 < 8):
            if(y-1 >= 0):
                if(board_state[x+2][y-1]%2 == BLACK or board_state[x+2][y-1] == 0):
                    move.append((x+2, y-1))
        if(x-2 >= 0):
            if(y+1 < 8):
                if(board_state[x-2][y+1]%2 == BLACK or board_state[x-2][y+1] == 0):
                    move.append((x-2, y+1))
        if(x-2 >= 0):
            if(y-1 >= 0):
                if(board_state[x-2][y-1]%2 == BLACK or board_state[x-2][y-1] == 0):
                    move.append((x-2, y-1))
        if(x+1 < 8):
            if(y+2 < 8):
                if(board_state[x+1][y+2]%2 == BLACK or board_state[x+1][y+2] == 0):
                    move.append((x+1, y+2))
        if(x+1 < 8):
            if(y-2 >= 0):
                if(board_state[x+1][y-2]%2 == BLACK or board_state[x+1][y-2] == 0):
                    move.append((x+1, y-2))
        if(x-1 >= 0):
            if(y+2 < 8):
                if(board_state[x-1][y+2]%2 == BLACK or board_state[x-1][y+2] == 0):
                    move.append((x-1, y+2))
        if(x-1 >= 0):
            if(y-2 >= 0):
                if(board_state[x-1][y-2]%2 == BLACK or board_state[x-1][y-2] == 0):
                    move.append((x-1, y-2))

    if(team == BLACK):
        if(x+2 < 8):
            if(y+1 < 8):
                if(board_state[x+2][y+1]%2 == WHITE):
                    move.append((x+2, y+1))
        if(x+2 < 8):
            if(y-1 >= 0):
                if(board_state[x+2][y-1]%2 == WHITE):
                    move.append((x+2, y-1))
        if(x-2 >= 0):
            if(y+1 < 8):
                if(board_state[x-2][y+1]%2 == WHITE):
                    move.append((x-2, y+1))
        if(x-2 >= 0):
            if(y-1 >= 0):
                if(board_state[x-2][y-1]%2 == WHITE):
                    move.append((x-2, y-1))
        if(x+1 < 8):
            if(y+2 < 8):
                if(board_state[x+1][y+2]%2 == WHITE):
                    move.append((x+1, y+2))
        if(x+1 < 8):
            if(y-2 >= 0):
                if(board_state[x+1][y-2]%2 == WHITE):
                    move.append((x+1, y-2))
        if(x-1 >= 0):
            if(y+2 < 8):
                if(board_state[x-1][y+2]%2 == WHITE):
                    move.append((x-1, y+2))
        if(x-1 >= 0):
            if(y-2 >= 0):
                if(board_state[x-1][y-2]%2 == WHITE):
                    move.append((x-1, y-2))

    return (x, y), move

def Bishop_move(board_state, team, x, y):

    move = []

    if(team == WHITE):
        i = 0
        while(True):
            if(x+i+1 < 8 and y+i+1 < 8):
                i = i+1
            else:
                break

            if(board_state[x+i][y+i]%2 == BLACK):
                move.append((x+i, y+i))
                break
            elif(board_state[x+i][y+i] == 0):
                move.append((x+i, y+i))
            else:
                break

        i = 0
        while(True):
            if(x-(i+1) >= 0 and y-(i+1) >= 0):
                i = i+1
            else:
                break

            if(board_state[x-i][y-i]%2 == BLACK):
                move.append((x-i, y-i))
                break
            elif(board_state[x-i][y-i] == 0):
                move.append((x-i, y-i))
            else:
                break

        i = 0
        while(True):
            if(x+i+1 < 8 and y-(i+1) >= 0):
                i = i+1
            else:
                break

            if(board_state[x+i][y-i]%2 == BLACK):
                move.append((x+i, y-i))
                break
            elif(board_state[x+i][y-i] == 0):
                move.append((x+i, y-i))
            else:
                break

        i = 0
        while(True):
            if(x-(i+1) >= 0 and y+i+1 < 8):
                i = i+1
            else:
                break

            if(board_state[x-i][y+i]%2 == BLACK):
                move.append((x-i, y+i))
                break
            elif(board_state[x-i][y+i] == 0):
                move.append((x-i, y+i))
            else:
                break

    if(team == BLACK):
        i = 0
        while(True):
            if(x+i+1 < 8 and y+i+1 < 8):
                i = i+1
            else:
                break

            if(board_state[x+i][y+i]%2 == WHITE and board_state[x+i][y+i] != 0):
                move.append((x+i, y+i))
                break
            elif(board_state[x+i][y+i] == 0):
                move.append((x+i, y+i))
            else:
                break

        i = 0
        while(True):
            if(x-(i+1) >= 0 and y-(i+1) >= 0):
                i = i+1
            else:
                break

            if(board_state[x-i][y-i]%2 == WHITE and board_state[x-i][y-i] != 0):
                move.append((x-i, y-i))
                break
            elif(board_state[x-i][y-i] == 0):
                move.append((x-i, y-i))
            else:
                break

        i = 0
        while(True):
            if(x+i+1 < 8 and y-(i+1) >= 0):
                i = i+1
            else:
                break

            if(board_state[x+i][y-i]%2 == WHITE and board_state[x+i][y-i] != 0):
                move.append((x+i, y-i))
                break
            elif(board_state[x+i][y-i] == 0):
                move.append((x+i, y-i))
            else:
                break

        i = 0
        while(True):
            if(x-(i+1) >= 0 and y+i+1 < 8):
                i = i+1
            else:
                break

            if(board_state[x-i][y+i]%2 == WHITE and board_state[x-i][y+i] != 0):
                move.append((x-i, y+i))
                break
            elif(board_state[x-i][y+i] == 0):
                move.append((x-i, y+i))
            else:
                break

    return (x, y), move

def Rook_move(board_state, team, x, y):

    move = []

    if(team == WHITE):
        i = 0
        while(True):
            if(x+i < 8):
                i = i+1
            else:
                break

            if(board_state[x+i][y]%2 == BLACK):
                move.append((x+i, y))
                break
            elif(board_state[x+i][y] == 0):
                move.append((x+i, y))
            else:
                break
        i = 0
        while(True):
            if(y+i < 8):
                i = i+1
            else:
                break

            if(board_state[x][y+1]%2 == BLACK):
                move.append((x, y+1))
                break
            elif(board_state[x][y+1] == 0):
                move.append((x, y+1))
            else:
                break

        i = 0
        while(True):
            if(x-i >= 0):
                i = i+1
            else:
                break

            if(board_state[x-i][y]%2 == BLACK):
                move.append((x-i, y))
                break
            elif(board_state[x-i][y] == 0):
                move.append((x-i, y))
            else:
                break
        i = 0
        while(True):
            if(y-i >= 0):
                i = i+1
            else:
                break

            if(board_state[x][y-i]%2 == BLACK):
                move.append((x, y-i))
                break
            elif(board_state[x][y-i] == 0):
                move.append((x, y-i))
            else:
                break

    if(team == BLACK):
        i = 0
        while(True):
            if(x+i < 8):
                i = i+1
            else:
                break

            if(board_state[x+i][y]%2 == WHITE and board_state[x+i][y] != 0):
                move.append((x+i, y))
                break
            elif(board_state[x+i][y] == 0):
                move.append((x+i, y))
            else:
                break
        i = 0
        while(True):
            if(y+i < 8):
                i = i+1
            else:
                break

            if(board_state[x][y+1]%2 == WHITE and board_state[x][y+i] != 0):
                move.append((x, y+1))
                break
            elif(board_state[x][y+1] == 0):
                move.append((x, y+1))
            else:
                break

        i = 0
        while(True):
            if(x-i >= 0):
                i = i+1
            else:
                break

            if(board_state[x-i][y]%2 == WHITE and board_state[x-i][y] != 0):
                move.append((x-i, y))
                break
            elif(board_state[x-i][y] == 0):
                move.append((x-i, y))
            else:
                break
        i = 0
        while(True):
            if(y-i >= 0):
                i = i+1
            else:
                break

            if(board_state[x][y-i]%2 == WHITE and board_state[x][y-i] != 0):
                move.append((x, y-i))
                break
            elif(board_state[x][y-i] == 0):
                move.append((x, y-i))
            else:
                break

    return (x, y), move

def Queen_move(board_state, team, x, y):

    move = []

    if(team == WHITE):
        i = 0
        while(True):
            if(x+i+1 < 8 and y+i+1 < 8):
                i = i+1
            else:
                break

            if(board_state[x+i][y+i]%2 == BLACK):
                move.append((x+i, y+i))
                break
            elif(board_state[x+i][y+i] == 0):
                move.append((x+i, y+i))
            else:
                break

        i = 0
        while(True):
            if(x-(i+1) >= 0 and y-(i+1) >= 0):
                i = i+1
            else:
                break

            if(board_state[x-i][y-i]%2 == BLACK):
                move.append((x-i, y-i))
                break
            elif(board_state[x-i][y-i] == 0):
                move.append((x-i, y-i))
            else:
                break

        i = 0
        while(True):
            if(x+i+1 < 8 and y-(i+1) >= 0):
                i = i+1
            else:
                break

            if(board_state[x+i][y-i]%2 == BLACK):
                move.append((x+i, y-i))
                break
            elif(board_state[x+i][y-i] == 0):
                move.append((x+i, y-i))
            else:
                break

        i = 0
        while(True):
            if(x-(i+1) >= 0 and y+i+1 < 8):
                i = i+1
            else:
                break

            if(board_state[x-i][y+i]%2 == BLACK):
                move.append((x-i, y+i))
                break
            elif(board_state[x-i][y+i] == 0):
                move.append((x-i, y+i))
            else:
                break

        i = 0
        while(True):
            if(x+i < 8):
                i = i+1
            else:
                break

            if(board_state[x+i][y]%2 == BLACK):
                move.append((x+i, y))
                break
            elif(board_state[x+i][y] == 0):
                move.append((x+i, y))
            else:
                break
        i = 0
        while(True):
            if(y+i < 8):
                i = i+1
            else:
                break

            if(board_state[x][y+1]%2 == BLACK):
                move.append((x, y+1))
                break
            elif(board_state[x][y+1] == 0):
                move.append((x, y+1))
            else:
                break

        i = 0
        while(True):
            if(x-i >= 0):
                i = i+1
            else:
                break

            if(board_state[x-i][y]%2 == BLACK):
                move.append((x-i, y))
                break
            elif(board_state[x-i][y] == 0):
                move.append((x-i, y))
            else:
                break
        i = 0
        while(True):
            if(y-i >= 0):
                i = i+1
            else:
                break

            if(board_state[x][y-i]%2 == BLACK):
                move.append((x, y-i))
                break
            elif(board_state[x][y-i] == 0):
                move.append((x, y-i))
            else:
                break

    if(team == BLACK):
        i = 0
        while(True):
            if(x+i+1 < 8 and y+i+1 < 8):
                i = i+1
            else:
                break

            if(board_state[x+i][y+i]%2 == WHITE and board_state[x+i][y+i] != 0):
                move.append((x+i, y+i))
                break
            elif(board_state[x+i][y+i] == 0):
                move.append((x+i, y+i))
            else:
                break

        i = 0
        while(True):
            if(x-(i+1) >= 0 and y-(i+1) >= 0):
                i = i+1
            else:
                break

            if(board_state[x-i][y-i]%2 == WHITE and board_state[x-i][y-i] != 0):
                move.append((x-i, y-i))
                break
            elif(board_state[x-i][y-i] == 0):
                move.append((x-i, y-i))
            else:
                break

        i = 0
        while(True):
            if(x+i+1 < 8 and y-(i+1) >= 0):
                i = i+1
            else:
                break

            if(board_state[x+i][y-i]%2 == WHITE and board_state[x+i][y-i] != 0):
                move.append((x+i, y-i))
                break
            elif(board_state[x+i][y-i] == 0):
                move.append((x+i, y-i))
            else:
                break

        i = 0
        while(True):
            if(x-(i+1) >= 0 and y+i+1 < 8):
                i = i+1
            else:
                break

            if(board_state[x-i][y+i]%2 == WHITE and board_state[x-i][y+i] != 0):
                move.append((x-i, y+i))
                break
            elif(board_state[x-i][y+i] == 0):
                move.append((x-i, y+i))
            else:
                break

        i = 0
        while(True):
            if(x+i < 8):
                i = i+1
            else:
                break

            if(board_state[x+i][y]%2 == WHITE and board_state[x+i][y] != 0):
                move.append((x+i, y))
                break
            elif(board_state[x+i][y] == 0):
                move.append((x+i, y))
            else:
                break
        i = 0
        while(True):
            if(y+i < 8):
                i = i+1
            else:
                break

            if(board_state[x][y+1]%2 == WHITE and board_state[x][y+i] != 0):
                move.append((x, y+1))
                break
            elif(board_state[x][y+1] == 0):
                move.append((x, y+1))
            else:
                break

        i = 0
        while(True):
            if(x-i >= 0):
                i = i+1
            else:
                break

            if(board_state[x-i][y]%2 == WHITE and board_state[x-i][y] != 0):
                move.append((x-i, y))
                break
            elif(board_state[x-i][y] == 0):
                move.append((x-i, y))
            else:
                break
        i = 0
        while(True):
            if(y-i >= 0):
                i = i+1
            else:
                break

            if(board_state[x][y-i]%2 == WHITE and board_state[x][y-i] != 0):
                move.append((x, y-i))
                break
            elif(board_state[x][y-i] == 0):
                move.append((x, y-i))
            else:
                break

    return (x, y), move

def King_move(board_state, team, x, y):

    move = []

    return (x, y), move

def Actions_List(board_state, team):

    action_list = []

    for i in range(8):
        for x in range(8):
            if(board_state[i][x]!=0 and board_state[i][x]%2==team):
                action_list.append()

    return action_list
