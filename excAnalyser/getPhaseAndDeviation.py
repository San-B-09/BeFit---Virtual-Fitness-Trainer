def phaseDifference(ref,curr):
    sum=0
    diff={}
    for i in ref.angles.keys():
        x=ref.angles[i]-curr.angles[i]
        diff[i]=x
        sum+=abs(x)
    return (sum,diff)

def getPhase(current,phases):
    mn=100000
    ind=-1
    diff=None
    for i in range(len(phases)):
        x,d=phaseDifference(phases[i],current)
        if x<mn: mn=x; ind=i; diff=d
    return (ind,diff)