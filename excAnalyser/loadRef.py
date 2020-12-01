import pose
import shelve

def loadReference(excercise:str):
    r=shelve.open("references\\"+excercise+"\\ref.db")
    frames=r['key']
    r.close()

    phases=[]
    for i in frames:
        if excercise=='squats':s=pose.squats.squats(i,0.20)
        elif excercise=='lunges':s=pose.lunges.lunges(i,0.20)
        phases.append(s)
    return phases


