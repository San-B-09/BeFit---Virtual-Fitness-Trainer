from pose.single import singlePoint
from pose.single import singleAngle

def getListPoints(d:dict):
    lst=[]
    for i in d.keys():
        lst.extend(list(i))
    lst=set(lst)
    return list(lst)

def takeBetter(x:singlePoint,y:singlePoint):
    if x.conf>y.conf:
        return x
    else:
        return y

def prepReduced(reduced,points):
    for i in reduced.keys():
        if i in points.keys():
            reduced[i]=points[i]
        else:
            reduced[i]=takeBetter(
                points['left_'+i],
                points['right_'+i]
                )
    return reduced

def prepAngles(angles,reduced):
    for i in angles.keys():
        # print("adkjfb")
        # print(reduced[i[0]])
        angles[i]=singleAngle(reduced[i[0]],reduced[i[1]],reduced[i[2]])
    return angles

def checkOkay(reduced,conf):
    for i in reduced.values():
        if i.conf < conf:
            return False
    return True