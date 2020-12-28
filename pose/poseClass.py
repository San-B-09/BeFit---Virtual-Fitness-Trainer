from pose.single import singlePoint
from pose import helpers

class pose:
    keyValues=['nose','left_eye','right_eye','left_ear','right_ear','left_shoulder',
             'right_shoulder','left_elbow','right_elbow','left_wrist','right_wrist',
             'left_hip','right_hip','left_knee','right_knee','left_ankle','right_ankle']
    points={}
    def createCoords(self,coordinates,conf):
        for i in range(len(self.keyValues)):
            self.points[self.keyValues[i]]=singlePoint(
                coordinates[i][0],
                coordinates[i][1],
                coordinates[i][2]
                )

    def addMoreInfo(self,image,diff,curr_phase,count):
        self.image=image
        self.diff=diff
        self.curr_phase=curr_phase
        self.count=count

    def updateAngleStatus(self,phases,tolerance):
        curr_ref_phase=phases[self.curr_phase]
        for i in self.angles.keys():
            self.angles[i].compareAngle(curr_ref_phase.angles[i],tolerance)

    def loadInfo(self):
        self.reduced=dict.fromkeys(helpers.getListPoints(self.angles),None)
        self.reduced=helpers.prepReduced(self.reduced,self.points)
        self.angles=helpers.prepAngles(self.angles,self.reduced)
        self.isOkay=helpers.checkOkay(self.reduced,self.conf)

    def __init__(self,coordinates,conf):
        self.createCoords(coordinates,conf)
        self.conf=conf