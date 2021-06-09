## Image Processing Function Code templates

import cv2
import numpy as np

## Template matching
# Ivan
def match_template(image,template,match_mode=0):

    tm_mode_dict = {0 : cv2.TM_CCOEFF, 1 : cv2.TM_CCOEFF_NORMED, 2 : cv2.TM_CCORR,
                    3 : cv2.TM_CCORR_NORMED, 4: cv2.TM_SQDIFF, 5 : cv2.TM_SQDIFF_NORMED}

    res = cv2.matchTemplate(image,template,tm_mode_dict[match_mode])  
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    w, h = template.shape[::-1]

    if match_mode in [4,5]:
        top_left = min_loc
        score = min_val
    else:
        top_left = max_loc
        score = max_val

    x1 = top_left[0]
    x2 = x1 + w
    y1 = top_left[1]
    y2 = y1 + h
    box = [x1,x2,y1,y2]

    return score,box


