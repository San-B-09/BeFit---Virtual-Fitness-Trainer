from pose.excerciseClass import *

def getObject(excercise: str, de, conf):
    s=None
    if excercise == 'squats':
        s = squats(de, conf)
    elif excercise == 'dumbbell_lateral_raises':
        s = dumbbell_lateral_raises(de, conf)
    elif excercise == 'dumbbell_upper_head':
        s = dumbbell_upper_head(de, conf)
    elif excercise == 'push_up':
        s = push_up(de, conf)
    return s
