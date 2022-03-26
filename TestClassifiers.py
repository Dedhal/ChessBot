import cv2
import numpy as np

processed_img = cv2.imread('img/board_infos/Boards_Examples/Board1.png')

Rook_mask = cv2.imread('img/board_infos/masks/Rook_mask.png')

W_Rook = cv2.imread('img/board_infos/W_Rook/W_Rook_wbg.png')

w, h = W_Rook.shape[:-1]

res = cv2.matchTemplate(processed_img, W_Rook, cv2.TM_CCOEFF_NORMED, mask = Rook_mask)
threshold = 0.99
loc = np.where(res >= threshold)
i = 0
for pt in zip(*loc[::-1]):  # Switch collumns and rows
    cv2.rectangle(processed_img, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)
    i = i+1
    print(pt[1])
print(loc)

Line = cv2.imread('img/board_infos/Board_Infos/Un.png')

h, w = Line.shape[:-1]

res = cv2.matchTemplate(processed_img, Line, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
i = 0
for pt in zip(*loc[::-1]):  # Switch collumns and rows
    cv2.rectangle(processed_img, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
    i = i+1
print(pt)

cv2.imwrite('result.png', processed_img)