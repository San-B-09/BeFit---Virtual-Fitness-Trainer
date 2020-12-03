import os
from posenet.singleImageDet import getDet
from pose.getAppropriateObject import getObject
import shelve
from copy import deepcopy

# file_name="references\\squats\\frame_0_delay-0.3s.jpg"

# lst=getDet(file_name)

# r=shelve.open("references\\squats\\ref.db")
# r['key']=lst
# r.close()

# r=shelve.open("references\\squats\\ref.db")
# for i in r['key']:
#     print(*i)
# r.close()

# refFolder=".\\references\\"
# for i in os.listdir(refFolder,conf):
    
#     lst=list(os.listdir(refFolder+i))
#     lst=[m for m in lst if "frame" in m]
#     lst.sort()

#     if len(lst)!=0:
#         refs=[]
#         for j in lst:
#             de=getDet(refFolder+i+"\\"+j)
#             refs.append(de)
#             for k in de:
#                 print(*k)
#             print(refFolder+i+"\\"+j,"==DONE")
#         r=shelve.open(refFolder+i+"\\ref.db")
#         r['key']=refs
#         r.close()

def getRefs(excercise:str,conf):
    refFolder=".\\references\\"+excercise
    lst=list(os.listdir(refFolder))
    lst=[m for m in lst if "frame" in m]
    lst.sort()
    refs=[]
    if len(lst)!=0:
        for j in lst:
            de=getDet(refFolder+"\\"+j)
            de=getObject(excercise,de,conf)
            refs.append(deepcopy(de))
    return refs
