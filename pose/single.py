class singlePoint:
    def __init__(self,x,y,conf):
        self.x=x
        self.y=y
        self.conf=conf
        
import numpy as np
class singleAngle:
    def __init__(self,first:singlePoint,sec:singlePoint,third:singlePoint):
        a = np.array([first.x,first.y])
        b = np.array([sec.x,sec.y])
        c = np.array([third.x,third.y])

        ba = a - b
        bc = c - b

        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        angle = np.arccos(cosine_angle)

        self.angle=np.degrees(angle)
        self.conf=min([first.conf,sec.conf,third.conf])