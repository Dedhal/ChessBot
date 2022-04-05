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

class Game:

    def __init__(self, board_state, team):
        self.last_board_state = None
        self.board_state = board_state
        self.team = team
        self.KingHasMoved = False
        self.ARookHasMoved = False
        self.HRookHasMoved = False

    #--------------------------- Def Pieces Moves -----------------------------#
    
    def Piece_move(self, team, x, y):
    
        move = []
    
        if(self.board_state[x][y]==W_BISHOP_VALUE or self.board_state[x][y]==B_BISHOP_VALUE):
            loop = FOUR_DIAG_DIRECTION
            movement_type = BRQ
        elif(self.board_state[x][y]==W_ROOK_VALUE or self.board_state[x][y]==B_ROOK_VALUE):
            loop = FOUR_MAIN_DIRECTION
            movement_type = BRQ
        elif(self.board_state[x][y]==W_QUEEN_VALUE or self.board_state[x][y]==B_QUEEN_VALUE):
            loop = EIGHT_DIRECTION
            movement_type = BRQ
        elif(self.board_state[x][y]==W_KNIGHT_VALUE or self.board_state[x][y]==B_KNIGHT_VALUE):
            loop = KNIGHT_DIRECTION
            movement_type = KK
        elif(self.board_state[x][y]==W_KING_VALUE or self.board_state[x][y]==B_KING_VALUE):
            loop = EIGHT_DIRECTION
            movement_type = KK
            #ROC
            if(not self.KingHasMoved):
                if(not self.ARookHasMoved):
                    if(not Is_in_check(Create_Board([x, y-1], x, y), team) and not Is_in_check(Create_Board([x, y-2], x, y), team)):
                        move.append((x, y-2))
            if(not self.KingHasMoved):
                if(not self.HRookHasMoved):
                    if(not Is_in_check(Create_Board([x, y+1], x, y), team) and not Is_in_check(Create_Board([x, y+2], x, y), team)):
                        move.append((x, y+2))
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
                                    if(self.board_state[x+direction[0]*i][y+direction[1]*i]%2 == ennemy_team and self.board_state[x+direction[0]*i][y+direction[1]*i] != 0):
                                        if(not Is_in_check(Create_Board([x+direction[0]*i, y+direction[1]*i], x, y), team)):
                                            move.append((x+direction[0]*i, y+direction[1]*i))
                                            break
                                        else:
                                            break
                                    elif(self.board_state[x+direction[0]*i][y+direction[1]*i] == 0):
                                        if(not Is_in_check(Create_Board([x+direction[0]*i, y+direction[1]*i], x, y), team)):
                                            move.append((x+direction[0]*i, y+direction[1]*i))
                                            break
                                        else:
                                            break
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
                        if(self.board_state[x+direction[0]][y+direction[1]]%2 == ennemy_team or self.board_state[x+direction[0]][y+direction[1]] == 0):
                            if(not Is_in_check(Create_Board([x+direction[0], y+direction[1]], x, y), team)):
                                move.append((x+direction[0], y+direction[1]))
    
        elif(movement_type == PAWN):
            if(team == WHITE):
                #First Move
                if(x == 1 and self.board_state[x+1][y] == 0 and self.board_state[x+2][y] == 0):
                    if(not Is_in_check(Create_Board([x+2, y], x, y), team)):
                        move.append((x+2, y))
                #Prise en passant
                if(x == 4):
                    if(y+1 < 8):
                        if(last_board_state[x+2][y+1] == B_PAWN_VALUE and last_board_state[x][y+1] == 0 and board_state[x+2][y+1] == 0 and board_state[x][y+1] == B_PAWN_VALUE):
                            move.append((x+1, y+1))
                    if(y-1 >= 0):
                        if(last_board_state[x+2][y-1] == B_PAWN_VALUE and last_board_state[x][y-1] == 0 and board_state[x+2][y-1] == 0 and board_state[x][y-1] == B_PAWN_VALUE):
                            move.append((x+1, y-1))
                #Take
                if(y+1 < 8):
                    if(board_state[x+1][y+1]%2 == BLACK):
                        if(not Is_in_check(Create_Board([x+1, y+1], x, y), team)):
                            move.append((x+1, y+1))
                if(y-1 >= 0):
                    if(board_state[x+1][y-1]%2 == BLACK):
                        if(not Is_in_check(Create_Board([x+1, y-1], x, y), team)):
                            move.append((x+1, y-1))
                #Push
                if(x+1 < 8):
                    if(board_state[x+1][y] == 0):
                        if(not Is_in_check(Create_Board([x+1, y], x, y), team)):
                            move.append((x+1, y))
    
            if(team == BLACK):
                #First Move
                if( x == 6 and board_state[x-1][y] == 0 and board_state[x-2][y] == 0):
                    if(not Is_in_check(Create_Board([x-2, y], x, y), team)):
                        move.append((x-2, y))
                #Prise en passant
                if(x == 3):
                    if(y+1 < 8):
                        if(last_board_state[x-2][y+1] == W_PAWN_VALUE and last_board_state[x][y+1] == 0 and board_state[x-2][y+1] == 0 and board_state[x][y+1] == W_PAWN_VALUE):
                            move.append((x-1, y+1))
                    if(y-1 >= 0):
                        if(last_board_state[x-2][y-1] == W_PAWN_VALUE and last_board_state[x][y-1] == 0 and board_state[x-2][y-1] == 0 and board_state[x][y-1] == W_PAWN_VALUE):
                            move.append((x-1, y-1))
                #Take
                if(y+1 < 8):
                    if(board_state[x-1][y+1] != 0 and board_state[x-1][y+1]%2 == WHITE):
                        if(not Is_in_check(Create_Board([x-1, y+1], x, y), team)):
                            move.append((x-1, y+1))
                if(y-1 >= 0):
                    if(board_state[x-1][y-1] != 0 and board_state[x-1][y-1]%2 == WHITE):
                        if(not Is_in_check(Create_Board([x-1, y-1], x, y), team)):
                            move.append((x-1, y-1))
                #Push
                if(x-1 >= 0):
                    if(board_state[x-1][y] == 0):
                        if(not Is_in_check(Create_Board([x-1, y], x, y), team)):
                            move.append((x-1, y))
    
        return (x, y), move
    
    def Is_in_check(self, tmp_board_state, team):
    
        move = []
    
        x, y = 0, 0
    
        for roi_x in range(8):
            for roi_y in range(8):
                if(team == WHITE):
                    if(tmp_board_state[roi_x][roi_y] == W_KING_VALUE):
                        x = roi_x
                        y = roi_y
                elif(team == BLACK):
                    if(tmp_board_state[roi_x][roi_y] == B_KING_VALUE):
                        x = roi_x
                        y = roi_y
    
    
        loop = FOUR_DIAG_DIRECTION
        for index, direction in enumerate(loop):
            for i in range(8):
                if(x+direction[0]*i < 8):
                    if(x+direction[0]*i >= 0):
                        if(y+direction[1]*i < 8):
                            if(y+direction[1]*i >= 0):
                                if(team == WHITE):
                                    if(tmp_board_state[x+direction[0]*i][y+direction[1]*i] == B_BISHOP_VALUE or tmp_board_state[x+direction[0]*i][y+direction[1]*i] == B_QUEEN_VALUE):
                                        move.append((x+direction[0]*i, y+direction[1]*i))
                                        break
                                    elif(tmp_board_state[x+direction[0]*i][y+direction[1]*i] == 0):
                                        continue
                                    else:
                                        break
                                if(team == BLACK):
                                    if(tmp_board_state[x+direction[0]*i][y+direction[1]*i] == W_BISHOP_VALUE or tmp_board_state[x+direction[0]*i][y+direction[1]*i] == W_QUEEN_VALUE):
                                        move.append((x+direction[0]*i, y+direction[1]*i))
                                        break
                                    elif(tmp_board_state[x+direction[0]*i][y+direction[1]*i] == 0):
                                        continue
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
    
        loop = FOUR_MAIN_DIRECTION
        for index, direction in enumerate(loop):
            for i in range(8):
                if(x+direction[0]*i < 8):
                    if(x+direction[0]*i >= 0):
                        if(y+direction[1]*i < 8):
                            if(y+direction[1]*i >= 0):
                                if(team == WHITE):
                                    if(tmp_board_state[x+direction[0]*i][y+direction[1]*i] == B_ROOK_VALUE or tmp_board_state[x+direction[0]*i][y+direction[1]*i] == B_QUEEN_VALUE):
                                        move.append((x+direction[0]*i, y+direction[1]*i))
                                        break
                                    elif(tmp_board_state[x+direction[0]*i][y+direction[1]*i] == 0):
                                        continue
                                    else:
                                        break
                                elif(team == BLACK):
                                    if(tmp_board_state[x+direction[0]*i][y+direction[1]*i] == W_ROOK_VALUE or tmp_board_state[x+direction[0]*i][y+direction[1]*i] == W_QUEEN_VALUE):
                                        move.append((x+direction[0]*i, y+direction[1]*i))
                                        break
                                    elif(tmp_board_state[x+direction[0]*i][y+direction[1]*i] == 0):
                                        continue
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
    
        loop = KNIGHT_DIRECTION
        for index, direction in enumerate(loop):
            if(x+direction[0] < 8 and x+direction[0] >= 0):
                if(y+direction[1] < 8 and y+direction[1] >=0):
                    if(team == WHITE):
                        if(tmp_board_state[x+direction[0]][y+direction[1]] == B_KNIGHT_VALUE):
                            move.append((x+direction[0], y+direction[1]))
                    elif(team == BLACK):
                        if(tmp_board_state[x+direction[0]][y+direction[1]] == W_KNIGHT_VALUE):
                            move.append((x+direction[0], y+direction[1]))
    
        if(team == WHITE):
            if(y+1 < 8):
                if(tmp_board_state[x+1][y+1] == B_PAWN_VALUE):
                    move.append((x+1, y+1))
            if(y-1 >= 0):
                if(tmp_board_state[x+1][y-1]%2 == B_PAWN_VALUE):
                    move.append((x+1, y-1))
    
        if(team == BLACK):
            if(y+1 < 8):
                if(tmp_board_state[x-1][y+1] == W_PAWN_VALUE):
                    move.append((x-1, y+1))
            if(y-1 >= 0):
                if(tmp_board_state[x-1][y-1] == W_PAWN_VALUE):
                    move.append((x-1, y-1))
    
        return move
    
    def Create_Board(self, move, x, y):
    
        tmp_board_state = self.board_state.copy()
        tmp_board_state[move[0]][move[1]] = self.board_state[x][y]
        tmp_board_state[x][y] = 0
    
        return tmp_board_state

    def Set_Last_Board_State(self, new_board_state):
        self.last_board_state = new_board_state.copy()

    def Set_Board_State(self, new_board_state):
        Set_Last_Board_State(self.board_state)
        self.board_state = new_board_state.copy()

    def ARookHasMoved(self):
        self.ARookHasMoved = True

    def HRookHasMoved(self):
        self.HRookHasMoved = True

    def KingHasMoved(self):
        self.KingHasMoved = True
    
    def Actions_List(self, team):
    
        action_list = []
    
        for i in range(8):
            for x in range(8):
                if(self.board_state[i][x]!=0 and self.board_state[i][x]%2==team):
                    action_list.append()
    
        return action_list
    