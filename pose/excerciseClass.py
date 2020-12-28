from pose.poseClass import pose
from pose import helpers

class dumbbell_lateral_raises(pose):
    angles={
        ('left_hip','left_shoulder','left_elbow'):None,
        ('right_hip','right_shoulder','right_elbow'):None,
        ('left_shoulder','left_elbow','left_wrist'):None,
        ('right_shoulder','right_elbow','right_wrist'):None
    }
    def __init__(self,coordinates,conf):
        pose.__init__(self,coordinates,conf)
        self.loadInfo()

class squats(pose):
    angles={
        ('nose','shoulder','hip'):None,
        ('shoulder','hip','knee'):None,
        ('hip','knee','ankle'):None
    }
    def __init__(self,coordinates,conf):
        pose.__init__(self,coordinates,conf)
        self.loadInfo()

class dumbbell_upper_head(pose):
    angles={
        ('right_shoulder','left_shoulder','left_elbow'):None,
        ('left_shoulder','right_shoulder','right_elbow'):None,
        ('right_shoulder','right_elbow','left_wrist'):None,
        ('right_shoulder','right_elbow','right_wrist'):None
    }
    def __init__(self,coordinates,conf):
        pose.__init__(self,coordinates,conf)
        self.loadInfo()

class push_up(pose):
    angles={
        # ('nose','shoulder','hip'):None,
        # ('shoulder','hip','knee'):None,
        # ('hip','knee','ankle'):None,
        ('shoulder','ankle','wrist'):None
    }
    def __init__(self,coordinates,conf):
        pose.__init__(self,coordinates,conf)
        self.loadInfo()

class sit_up(pose):
    angles={
        ('nose','shoulder','hip'):None,
        ('hip','knee','ankle'):None,
        ('shoulder','hip','knee'):None,
    }
    def __init__(self,coordinates,conf):
        pose.__init__(self,coordinates,conf)
        self.loadInfo()

class bicep_press(pose):
    angles={
        ('shoulder','elbow','wrist'):None
    }
    def __init__(self,coordinates,conf):
        pose.__init__(self,coordinates,conf)
        self.loadInfo()