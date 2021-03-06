import copy

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
        self.last_board_state = board_state
        self.board_state = board_state
        self.team = team
        self.KingHasMoved = False
        self.ARookHasMoved = False
        self.HRookHasMoved = False
        self.LastPawnMove = 0
        self.NumMove = 0
        self.LastCapture = 0
        self.Repetition = 0

    #--------------------------- Def Pieces Moves -----------------------------#
    
    def Piece_move(self, x, y):
    
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
                    if(self.board_state[x][y-1] == 0 and self.board_state[x][y-2] == 0):
                        if(not self.Is_in_check(self.Create_Board([x, y-1], x, y)) and not self.Is_in_check(Create_Board([x, y-2], x, y))):
                            move.append((x, y-2))
            if(not self.KingHasMoved):
                if(not self.HRookHasMoved):
                    if(self.board_state[x][y+1] == 0 and self.board_state[x][y+2] == 0):
                        if(not self.Is_in_check(self.Create_Board([x, y+1], x, y)) and not self.Is_in_check(Create_Board([x, y+2], x, y))):
                            move.append((x, y+2))
        else:
            movement_type = PAWN
    
        if(self.team == WHITE):
            ennemy_team = BLACK
        elif(self.team == BLACK):
            ennemy_team = WHITE
    
        if(movement_type == BRQ):
            for index, direction in enumerate(loop):
                for i in range(8):
                    if(x+direction[0]*i < 8):
                        if(x+direction[0]*i >= 0):
                            if(y+direction[1]*i < 8):
                                if(y+direction[1]*i >= 0):
                                    if(self.board_state[x+direction[0]*i][y+direction[1]*i]%2 == ennemy_team and self.board_state[x+direction[0]*i][y+direction[1]*i] != 0):
                                        if(not self.Is_in_check(self.Create_Board([x+direction[0]*i, y+direction[1]*i], x, y))):
                                            move.append((x+direction[0]*i, y+direction[1]*i))
                                            break
                                        else:
                                            break
                                    elif(self.board_state[x+direction[0]*i][y+direction[1]*i] == 0):
                                        if(not self.Is_in_check(self.Create_Board([x+direction[0]*i, y+direction[1]*i], x, y))):
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
                            if(not self.Is_in_check(self.Create_Board([x+direction[0], y+direction[1]], x, y))):
                                move.append((x+direction[0], y+direction[1]))
    
        elif(movement_type == PAWN):
            if(self.team == WHITE):
                #First Move
                if(x == 1 and self.board_state[x+1][y] == 0 and self.board_state[x+2][y] == 0):
                    if(not self.Is_in_check(self.Create_Board([x+2, y], x, y))):
                        move.append((x+2, y))
                #Prise en passant
                if(x == 4):
                    if(y+1 < 8):
                        if(self.last_board_state[x+2][y+1] == B_PAWN_VALUE and self.last_board_state[x][y+1] == 0 and self.board_state[x+2][y+1] == 0 and self.board_state[x][y+1] == B_PAWN_VALUE):
                            if(not self.Is_in_check(self.Create_Board([x+1, y+1], x, y))):
                                move.append((x+1, y+1))
                    if(y-1 >= 0):
                        if(self.last_board_state[x+2][y-1] == B_PAWN_VALUE and self.last_board_state[x][y-1] == 0 and self.board_state[x+2][y-1] == 0 and self.board_state[x][y-1] == B_PAWN_VALUE):
                            if(not self.Is_in_check(self.Create_Board([x+1, y-1], x, y))):
                                move.append((x+1, y-1))
                #Take
                if(y+1 < 8):
                    if(self.board_state[x+1][y+1]%2 == BLACK):
                        if(not self.Is_in_check(self.Create_Board([x+1, y+1], x, y))):
                            move.append((x+1, y+1))
                if(y-1 >= 0):
                    if(self.board_state[x+1][y-1]%2 == BLACK):
                        if(not self.Is_in_check(self.Create_Board([x+1, y-1], x, y))):
                            move.append((x+1, y-1))
                #Push
                if(x+1 < 8):
                    if(self.board_state[x+1][y] == 0):
                        if(not self.Is_in_check(self.Create_Board([x+1, y], x, y))):
                            move.append((x+1, y))
    
            if(self.team == BLACK):
                #First Move
                if( x == 6 and self.board_state[x-1][y] == 0 and self.board_state[x-2][y] == 0):
                    if(not self.Is_in_check(self.Create_Board([x-2, y], x, y))):
                        move.append((x-2, y))
                #Prise en passant
                if(x == 3):
                    if(y+1 < 8):
                        if(self.last_board_state[x-2][y+1] == W_PAWN_VALUE and self.last_board_state[x][y+1] == 0 and self.board_state[x-2][y+1] == 0 and self.board_state[x][y+1] == W_PAWN_VALUE):
                            if(not self.Is_in_check(self.Create_Board([x-1, y+1], x, y))):
                                move.append((x-1, y+1))
                    if(y-1 >= 0):
                        if(self.last_board_state[x-2][y-1] == W_PAWN_VALUE and self.last_board_state[x][y-1] == 0 and self.board_state[x-2][y-1] == 0 and self.board_state[x][y-1] == W_PAWN_VALUE):
                            if(not self.Is_in_check(self.Create_Board([x-1, y-1], x, y))):
                                move.append((x-1, y-1))
                #Take
                if(y+1 < 8):
                    if(self.board_state[x-1][y+1] != 0 and self.board_state[x-1][y+1]%2 == WHITE):
                        if(not self.Is_in_check(self.Create_Board([x-1, y+1], x, y))):
                            move.append((x-1, y+1))
                if(y-1 >= 0):
                    if(self.board_state[x-1][y-1] != 0 and self.board_state[x-1][y-1]%2 == WHITE):
                        if(not self.Is_in_check(self.Create_Board([x-1, y-1], x, y))):
                            move.append((x-1, y-1))
                #Push
                if(x-1 >= 0):
                    if(self.board_state[x-1][y] == 0):
                        if(not self.Is_in_check(self.Create_Board([x-1, y], x, y))):
                            move.append((x-1, y))
    
        return move
    
    def Is_in_check(self, tmp_board_state):
    
        x, y = 0, 0
    
        for roi_x in range(8):
            for roi_y in range(8):
                if(self.team == WHITE):
                    if(tmp_board_state[roi_x][roi_y] == W_KING_VALUE):
                        x = roi_x
                        y = roi_y
                elif(self.team == BLACK):
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
                                if(self.team == WHITE):
                                    if(tmp_board_state[x+direction[0]*i][y+direction[1]*i] == B_BISHOP_VALUE or tmp_board_state[x+direction[0]*i][y+direction[1]*i] == B_QUEEN_VALUE):
                                        return True
                                    elif(tmp_board_state[x+direction[0]*i][y+direction[1]*i] == 0):
                                        continue
                                    else:
                                        break
                                if(self.team == BLACK):
                                    if(tmp_board_state[x+direction[0]*i][y+direction[1]*i] == W_BISHOP_VALUE or tmp_board_state[x+direction[0]*i][y+direction[1]*i] == W_QUEEN_VALUE):
                                        return True
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
                                if(self.team == WHITE):
                                    if(tmp_board_state[x+direction[0]*i][y+direction[1]*i] == B_ROOK_VALUE or tmp_board_state[x+direction[0]*i][y+direction[1]*i] == B_QUEEN_VALUE):
                                        return True
                                    elif(tmp_board_state[x+direction[0]*i][y+direction[1]*i] == 0):
                                        continue
                                    else:
                                        break
                                elif(self.team == BLACK):
                                    if(tmp_board_state[x+direction[0]*i][y+direction[1]*i] == W_ROOK_VALUE or tmp_board_state[x+direction[0]*i][y+direction[1]*i] == W_QUEEN_VALUE):
                                        return True
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
                    if(self.team == WHITE):
                        if(tmp_board_state[x+direction[0]][y+direction[1]] == B_KNIGHT_VALUE):
                            return True
                    elif(self.team == BLACK):
                        if(tmp_board_state[x+direction[0]][y+direction[1]] == W_KNIGHT_VALUE):
                            return True
    
        if(self.team == WHITE):
            if(y+1 < 8 and x+1 < 8):
                if(tmp_board_state[x+1][y+1] == B_PAWN_VALUE):
                    return True
            if(y-1 >= 0 and x+1 < 8):
                if(tmp_board_state[x+1][y-1]%2 == B_PAWN_VALUE):
                    return True
    
        if(self.team == BLACK):
            if(y+1 < 8):
                if(tmp_board_state[x-1][y+1] == W_PAWN_VALUE):
                    return True
            if(y-1 >= 0):
                if(tmp_board_state[x-1][y-1] == W_PAWN_VALUE):
                    return True
    
        return False

    #TODO
    def Is_Draw(self):
        # Pat
        if(self.Actions_List() == None and not self.Is_In_Check(self.board_state)):
            return True

        # Manque de materiel
        powerful_piece_alive = False
        for line in self.board_state:
            for case in line:
                if(case == B_ROOK_VALUE or case == W_ROOK_VALUE or case == B_QUEEN_VALUE or case == W_QUEEN_VALUE or case == B_PAWN_VALUE or case == W_PAWN_VALUE):
                    powerful_piece_alive = True
                    break
                    
            if(powerful_piece_alive):
                break

        white_minors = 0
        black_minors = 0
        if(not powerful_piece_alive):
            for line in self.board_state:
                for case in line:
                    if(case == W_BISHOP_VALUE or case == W_KNIGHT_VALUE):
                        white_minors = white_minors + 1
                    if(case == B_BISHOP_VALUE or case == B_KNIGHT_VALUE):
                        black_minors = black_minors + 1

            if(white_minors < 2 and black_minors < 2):
                return True

        # R??gle des 50 coups
        if(self.NumMove - 50 >= self.LastCapture and self.NumMove - 50 >= self.LastPawnMove):
            return True

        # R??p??tition / ??chec perpetuel
        if(self.Repetition >= 3):
            return True
        
    
    def Create_Board(self, move, x, y):
    
        tmp_board_state = copy.deepcopy(self.board_state)
        tmp_board_state[move[0]][move[1]] = self.board_state[x][y]
        tmp_board_state[x][y] = 0
    
        return tmp_board_state

    def Set_Last_Board_State(self, new_board_state):
        self.last_board_state = new_board_state.copy()

    def Set_Board_State(self, new_board_state):
        # Counting moves
        self.NumMove = self.NumMove + 1

        # Remembering when a piece was captured for the last time
        NumPieces = 0
        for line in self.board_state:
            for case in line:
                if(case != 0):
                    NumPieces = NumPieces + 1

        New_NumPieces = 0
        for line in new_board_state:
            for case in line:
                if(case != 0):
                    New_NumPieces = New_NumPieces + 1

        if(New_NumPieces != NumPieces):
            self.LastCapture = self.NumMove

        # Remembering last pawn move
        for i in range(8):
            for j in range(8):
                if((self.board_state[i][j] == W_PAWN_VALUE or self.board_state[i][j] == B_PAWN_VALUE) and new_board_state[i][j] == 0):
                    self.LastPawnMove = self.NumMove
                    break

            if(self.LastPawnMove == self.NumMove):
                break

        # Counting Repetitions
        if(self.last_board_state.all() == new_board_state.all()):
            self.Repetition = self.Repetition + 1
        else:
            self.Repetition = 0

        # Update Board
        self.Set_Last_Board_State(self.board_state)
        self.board_state = new_board_state.copy()

    # TODO
    def ARookHasMoved(self):
        self.ARookHasMoved = True

    def HRookHasMoved(self):
        self.HRookHasMoved = True

    def KingHasMoved(self):
        self.KingHasMoved = True

    #___________________________#

    def Get_Board_State():
        return board_state
    
    def Actions_List(self):
    
        action_list = []
        piece_coordinates = []
        target_coordinates = []
    
        for x in range(8):
            for y in range(8):
                if(self.board_state[x][y]!=0 and self.board_state[x][y]%2==self.team):
                    moves = self.Piece_move(x, y)
                    print(moves)
                    for move in moves:
                        action_board = self.Create_Board(move, x, y).copy()
                        action_list.append(action_board)
                        target_coordinates.append(move)
                        piece_coordinates.append((x, y))

    
        return action_list, piece_coordinates, target_coordinates