import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import ReleaseKey, PressKey, Mouse, Make_move

import matplotlib.image as mpimg
import keras
from skimage import io, transform
from skimage.util.shape import view_as_blocks

import CheckPieces as cp
import PiecesMoves as pm

input("Appuyez sur entrer pour commencer")

# Initialisation CNN

piece_symbols = ' pPnNbBrRqQkK'

def onehot_from_fen(fen):
    eye = np.eye(13)
    output = np.empty((0, 13))
    fen = re.sub('[-]', '', fen)

    for char in fen:
        if char in '12345678':
            output = np.append(output, np.tile(eye[12], (int(char), 1)), axis = 0)
        else:
            idx = piece_symbols.index(char)
            output = np.append(output, eye[idx].reshape((1, 13)), axis = 0)

    return output

def fen_from_onehot(onehot):
    output = ''
    for j in range(8):
        for i in range(8):
            output += piece_symbols[onehot[j][i]]
        if j != 7:
            output += '-'

    for i in range(8, 0, -1):
        output = output.replace(' ' * i, str(i))

    return output

def process_image(img):
    downsample_size = 200
    square_size = int(downsample_size/8)
    img_read = img
    img_read = transform.resize(img_read, (downsample_size, downsample_size), mode='constant')
    img_read = np.array(img_read)
    img_read.reshape(200,200, -1)
    tiles = view_as_blocks(img_read, block_shape=(square_size, square_size, 3))
    tiles = tiles.squeeze(axis=2)
    return tiles.reshape(64, square_size, square_size, 3)

print("Loading model...")
model = keras.models.load_model('chess_model_TD100000_VD20000_Basic-CNN.h5py')

while(True):

    last_time = time.time()


    # Tour
    screen = np.array(ImageGrab.grab(bbox=(350,165,1215,1020)))
    # PC Portable
    # screen = np.array(ImageGrab.grab(bbox=(270,170,1132,1020)))

    team, screen = cp.Initialize_Board(screen)
    print(team)
    game = None

    while(True):
        # Tour
        screen = np.array(ImageGrab.grab(bbox=(408,170,1215,983)))
        # PC Portable
        # screen = np.array(ImageGrab.grab(bbox=(270,170,1132,1020)))

        board_state = model.predict(process_image(screen)).argmax(axis=1).reshape(-1, 8, 8)
        
        print(board_state[0])
        #new_screen, board_state = cp.GetBoardState(screen, team)
        if(game == None):
            game = pm.Game(board_state[0], team)
        else:
            game.Set_Board_State(board_state[0])

        print(game.Actions_List())

        #Make_move(team, (6, 4), (4, 4))
        #break

        print('Loop time : {}s'.format(time.time()-last_time))
        last_time = time.time()



        #cv2.imshow('window2', screen)



        # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
