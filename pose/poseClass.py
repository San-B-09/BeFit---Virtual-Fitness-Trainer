from pose.single import singlePoint

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

    def __init__(self,coordinates,conf):
        self.createCoords(coordinates,conf)
        self.conf=conf
    

# coords=[[0,0,100] for i in range(17)]
# p1=pose(coords,50)
# for i in p1.coordinates.keys():
#     print(i,p1.coordinates[i].x)