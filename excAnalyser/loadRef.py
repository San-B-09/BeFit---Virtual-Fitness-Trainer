from pose.getAppropriateObject import getObject
import shelve

def loadReference(excercise:str,conf):
    r=shelve.open("references\\"+excercise+"\\ref.db")
    frames=r['key']
    r.close()

    phases=[]
    for i in frames:
        s=getObject(excercise,i,conf)
        phases.append(s)
    return phases


