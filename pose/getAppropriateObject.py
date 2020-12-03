from pose.squats import squats
from pose.lunges import lunges
def getObject(excercise: str, de, conf):
    s=None
    if excercise == 'squats':
        s = squats(de, conf)
    elif excercise == 'lunges':
        s = lunges(de, conf)
    return s
