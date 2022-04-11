import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import ReleaseKey, PressKey, Mouse, Make_move

import CheckPieces as cp
import PiecesMoves as pm

input("Appuyez sur entrer pour commencer")

while(True):

    last_time = time.time()

    screen = np.array(ImageGrab.grab(bbox=(350,165,1215,1020)))
    

    input("Appuyez sur entrer pour commencer")

    team, screen = cp.Initialize_Board(screen)
    print(team)
    game = None

    while(True):
        screen = np.array(ImageGrab.grab(bbox=(350,165,1215,1020)))
        
        new_screen, board_state = cp.GetBoardState(screen, team)
        if(game == None):
            game = pm.Game(board_state, team)
        else:
            game.Set_Board_State(board_state)

        print(game.Actions_List())

        Make_move(team, (6, 4), (4, 4))
        break

        print('Loop time : {}s'.format(time.time()-last_time))
        last_time = time.time()



        cv2.imshow('window2', new_screen)



        # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
