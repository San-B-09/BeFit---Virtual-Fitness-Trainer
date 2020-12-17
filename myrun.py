import tensorflow as tf
import cv2
import os

import posenet
from posenet.singleImageDet import getFastDet

from pose.getAppropriateObject import getObject
from references.prepReference import getRefs
from excAnalyser.getPhaseAndDeviation import getPhase
from excAnalyser.countReps import countReps
from excAnalyser.genReport import GenRep
from writeOnImage import write


cam_id = 0
cam_id="demo\\squats_test.mp4"
cam_id="demo\\mydemo.mp4"
cam_width = 360
cam_height = 280
scale_factor = 0.5
model_name = 101
conf=0.1
phase_list=[]
count=0

def getExcerciseName():
    temp_cnt=1
    excercises=[i for i in os.listdir(".\\references\\") if ("." not in i) and ("__" not in i)]
    for i in excercises:
        print(str(temp_cnt)+".\t"+i)
        temp_cnt+=1
    return excercises[int(input("\nEnter index of excercise: "))-1]

with tf.Session() as sess:

    model_cfg, model_outputs=posenet.load_model(model_name,sess)
    output_stride=model_cfg['output_stride']

    excercise=getExcerciseName()
    phases=getRefs(excercise,conf)

    data=[]
    cap  =  cv2.VideoCapture(cam_id)
    # cap.set(3,cam_width)
    # cap.set(4,cam_height)
    check_read=0
    curr_phase=-1
    while True:
        if check_read==0:
            try:
                lst, image = getFastDet(cap, scale_factor, output_stride, sess, model_outputs,conf)
            except:
                break
            check_read+=4
        else:
            try:
                posenet.read_cap(cap, scale_factor=scale_factor, output_stride=output_stride)
            except:
                break
            check_read-=1
            continue

        s = getObject(excercise, lst, conf)

        if s.isOkay:
            curr_phase,diff=getPhase(s,phases)
            phase_list.append(curr_phase)
            temp=countReps(phase_list,len(phases))
            if len(temp)<len(phase_list):
                count+=1
            phase_list=temp
            s.addMoreInfo(image,diff,curr_phase,count)
            data.append(s)


        image=write(image,s,curr_phase,count,len(phases))

        cv2.imshow('RepCounter', image)

        ch  =  cv2.waitKey(1)
        if(ch == ord('q') or ch == ord('Q')):break
        if(ch == ord('r') or ch == ord('R')):count=0

    rep=GenRep(data,phases)

    cap.release()
    cv2.destroyAllWindows()