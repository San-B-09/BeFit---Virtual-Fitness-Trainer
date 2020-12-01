from pose.squats import squats
import shelve

r=shelve.open("references\\squats\\ref.db")
frames=r['key']
r.close()

phases=[]
for i in frames:
    s=squats(i,0.25)
    for j in s.reduced.keys():
        print(j,int(s.reduced[j].x),int(s.reduced[j].y),int(s.reduced[j].conf*100))
    for k in s.angles.keys():
        print(k,s.angles[k].angle,s.angles[k].conf)
    print("-"*50)


