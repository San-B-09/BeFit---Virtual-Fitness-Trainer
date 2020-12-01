import os
from singleImageDet import getDet
import shelve

# file_name="references\\squats\\frame_0_delay-0.3s.jpg"

# lst=getDet(file_name)
# # for i in lst:
# #     print(*i)

# r=shelve.open("references\\squats\\ref.db")
# r['key']=lst
# r.close()

# r=shelve.open("references\\squats\\ref.db")
# for i in r['key']:
#     print(*i)
# r.close()
refFolder=".\\references\\"
for i in os.listdir(refFolder):
    
    lst=list(os.listdir(refFolder+i))
    lst=[m for m in lst if "frame" in m]
    lst.sort()

    if len(lst)!=0:
        refs=[]
        for j in lst:
            refs.append(getDet(refFolder+i+"\\"+j))
            print(refFolder+i+"\\"+j,"==DONE")
        r=shelve.open(refFolder+i+"\\ref.db")
        r['key']=refs
        r.close()

