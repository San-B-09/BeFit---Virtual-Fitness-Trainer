from pose.poseClass import pose
from pose import helpers

class squats(pose):
    angles={
        ('nose','shoulder','hip'):None,
        ('shoulder','hip','knee'):None,
        ('hip','knee','ankle'):None
    }

    reduced={
        'nose':None,
        'shoulder':None,
        'hip':None,
        'ankle':None,
        'knee':None
        }

    def __init__(self,coordinates,conf):
        pose.__init__(self,coordinates,conf)
        self.reduced=helpers.prepReduced(self.reduced,self.points)
        self.angles=helpers.prepAngles(self.angles,self.reduced)
        self.isOkay=helpers.checkOkay(self.reduced,self.conf)

# coords=[[0,0,100] for i in range(17)]
# p1=squats(coords,50)
# for i in p1.points.keys():
#     print(i,p1.points[i].x)