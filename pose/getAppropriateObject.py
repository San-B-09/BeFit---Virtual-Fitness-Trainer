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
    elif excercise == 'sit_up':
        s = sit_up(de, conf)
    elif excercise == 'bicep_press':
        s = bicep_press(de, conf)
    return s
