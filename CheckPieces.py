import cv2
import numpy as np

#------------------------------ Loading Masks -----------------------------#

PAWN_MASK = cv2.imread('img/board_infos/masks/Pawn_mask.png')
ROOK_MASK = cv2.imread('img/board_infos/masks/Rook_mask.png')
QUEEN_MASK = cv2.imread('img/board_infos/masks/Queen_mask.png')
KNIGHT_MASK = cv2.imread('img/board_infos/masks/Knight_mask.png')
KING_MASK = cv2.imread('img/board_infos/masks/King_mask.png')
BISHOP_MASK = cv2.imread('img/board_infos/masks/Bishop_mask.png')

MASKS = [PAWN_MASK, ROOK_MASK, QUEEN_MASK, KNIGHT_MASK, KING_MASK, BISHOP_MASK]

#----------------------------- Loading Models -----------------------------#

W_PAWN = cv2.imread('img/board_infos/W_Pawn/W_Pawn_wbg.png')
W_ROOK = cv2.imread('img/board_infos/W_Rook/W_Rook_wbg.png')
W_QUEEN = cv2.imread('img/board_infos/W_Queen/W_Queen_wbg.png')
W_KNIGHT = cv2.imread('img/board_infos/W_Knight/W_Knight_wbg.png')
W_KING = cv2.imread('img/board_infos/W_King/W_King_wbg.png')
W_BISHOP = cv2.imread('img/board_infos/W_Bishop/W_Bishop_wbg.png')

B_PAWN = cv2.imread('img/board_infos/B_Pawn/B_Pawn_wbg.png')
B_ROOK = cv2.imread('img/board_infos/B_Rook/B_Rook_wbg.png')
B_QUEEN = cv2.imread('img/board_infos/B_Queen/B_Queen_wbg.png')
B_KNIGHT = cv2.imread('img/board_infos/B_Knight/B_Knight_wbg.png')
B_KING = cv2.imread('img/board_infos/B_King/B_King_wbg.png')
B_BISHOP = cv2.imread('img/board_infos/B_Bishop/B_Bishop_wbg.png')

MODELS = [W_PAWN, W_ROOK, W_QUEEN, W_KNIGHT, W_KING, W_BISHOP, B_PAWN, B_ROOK, B_QUEEN, B_KNIGHT, B_KING, B_BISHOP]

#------------------------------- Constants --------------------------------#

ALLY_COLOR = (255, 0, 0)
ENNEMY_COLOR = (0, 0, 255)

WHITE = 0
BLACK = 1

LINES = [719, 617, 515, 413, 311, 209, 107, 5]
COLUMNS = [49, 151, 253, 355, 457, 559, 661, 763]

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

PIECES_VALUES = [W_PAWN_VALUE, W_ROOK_VALUE, W_QUEEN_VALUE, W_KNIGHT_VALUE, W_KING_VALUE, W_BISHOP_VALUE, B_PAWN_VALUE, B_ROOK_VALUE, B_QUEEN_VALUE, B_KNIGHT_VALUE, B_KING_VALUE, B_BISHOP_VALUE]

#---------------------------- Get Actual Team -----------------------------#

def Get_Team_Color(image):

    Line = cv2.imread('img/board_infos/Board_Infos/Un.png')

    h, w = Line.shape[:-1]

    res = cv2.matchTemplate(image, Line, cv2.TM_CCOEFF_NORMED)
    threshold = 0.95
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
    print(loc)

    if(loc[0] == 719):
        return WHITE, image
    else:
        return BLACK, image

#---------------------------- Initialize Board ----------------------------#

def Initialize_Board(image):

    color = Get_Team_Color(image)

    return color

#--------------------------- Update Game State ----------------------------#

def GetBoardState(original_image, team) :

    processed_img = original_image
    board_state = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

    #------------------------------ White Pawns ------------------------------#

    w, h = 100, 100

    for i in range(12):

        res = cv2.matchTemplate(processed_img, MODELS[i], cv2.TM_CCOEFF_NORMED, mask = MASKS[i%6])

        if(i==5):
            threshold=0.85
        else:
            threshold = 0.99

        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):  # Switch collumns and rows
            for line in LINES:
                if(pt[1]==line):
                    for column in COLUMNS:
                        if(pt[0]==column):
                            if(team == WHITE and i < 6):
                                cv2.rectangle(processed_img, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)
                            elif(team == WHITE and i >= 6):
                                cv2.rectangle(processed_img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                            elif(team == BLACK and i < 6):
                                cv2.rectangle(processed_img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                            else:
                                cv2.rectangle(processed_img, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)
            
                        
                            x, y = Get_Coordinates(pt, team)
                            board_state[x][y] = PIECES_VALUES[i]

    print(board_state)

    return processed_img, board_state


#---------------------------- Def Coordinates -----------------------------#

def Get_Coordinates(pt, team):

    nums = [0, 1, 2, 3, 4, 5, 6, 7]

    if(team == BLACK):
        nums.reverse()
        
    for i in range(8):
        if(pt[1] == LINES[i]):
            for x in range(8):
                if(pt[0] == COLUMNS[x]):
                    return nums[i], nums[x]

