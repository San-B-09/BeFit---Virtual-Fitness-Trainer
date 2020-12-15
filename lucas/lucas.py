import cv2
import numpy as np


def getDet(old_frame,curr_frame,p0):
    lk_params = dict(
        winSize=(10,10),
        maxLevel=2,
        criteria=(
            (
                cv2.TERM_CRITERIA_EPS |
                cv2.TERM_CRITERIA_COUNT
                ),
            10,
            0.03
            )
        )
    old_gray=cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)
    frame_gray=cv2.cvtColor(curr_frame,cv2.COLOR_BGR2GRAY)
    p=p0.reshape((-1,1,2)).astype(np.float32)
    p1,st,err=cv2.calcOpticalFlowPyrLK(old_gray,frame_gray,p,None,**lk_params)
    good_new=p1[st==1]
    return good_new.reshape((1,-1,2))