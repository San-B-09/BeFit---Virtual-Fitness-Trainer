from pose.squats import squats
from pose.lunges import lunges
def getObject(excercise: str, i, conf):
    s=None
    if excercise == 'squats':
        s = squats(i, conf)
    elif excercise == 'lunges':
        s = lunges(i, conf)
    return s
