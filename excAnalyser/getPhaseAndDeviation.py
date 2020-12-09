def phaseDifference(ref,curr):
    sum=0.0
    diff={}
    for i in ref.angles.keys():
        x=ref.angles[i].angle-curr.angles[i].angle
        diff[i]=x
        sum+=abs(x)
    return (sum,diff)

def getPhase(current,phases):
    mn=100000
    ind=-1
    diff=None
    for i in range(len(phases)):
        x,d=phaseDifference(phases[i],current)
        # print(x,d)
        if x<mn:
            mn=x
            ind=i
            diff=d
    return (ind,diff)
