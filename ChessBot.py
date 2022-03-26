import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import ReleaseKey, PressKey, Mouse

import CheckPieces as cp

last_time = time.time()

screen = np.array(ImageGrab.grab(bbox=(350,165,1215,1020)))

team = cp.Initialize_Board(screen)

while(True):
        screen = np.array(ImageGrab.grab(bbox=(350,165,1215,1020)))
        
        new_screen, board_state = cp.GetBoardState(screen, team)

        print('Loop time : {}s'.format(time.time()-last_time))
        last_time = time.time()



        cv2.imshow('window2', new_screen)



        # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
