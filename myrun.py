import tensorflow as tf
import cv2

import posenet
from posenet.singleImageDet import getFastDet

from pose.getAppropriateObject import getObject
from prepReference import getRefs
from excAnalyser.getPhaseAndDeviation import getPhase
from excAnalyser.loadRef import loadReference
from excAnalyser.countReps import countReps
from writeOnImage import write

cam_id = 0
cam_id="demo\\squats_test.mp4"
cam_width = 1080
cam_height = 720
scale_factor = 0.7125
model_name = 101
conf=0.1
phase_list=[]
count=0

with tf.Session() as sess:

    model_cfg, model_outputs=posenet.load_model(model_name,sess)
    output_stride=model_cfg['output_stride']

    # excercise = input("Name of excercise: ")
    excercise='squats'
    phases=getRefs(excercise,conf)

    cap  =  cv2.VideoCapture(cam_id)
    cap.set(3,cam_width)
    cap.set(4,cam_height)

    while True:
        try:
            lst, image = getFastDet(cap, scale_factor, output_stride, sess, model_outputs,conf)
        except:
            break
        s = getObject(excercise, lst, conf)

        if s.isOkay:
            curr_phase,diff=getPhase(s,phases)
            phase_list.append(curr_phase)
            temp=countReps(phase_list,len(phases))
            if len(temp)<len(phase_list):
                count+=1
            phase_list=temp

        image=write(image,s,curr_phase,count,len(phases))

        cv2.imshow('RepCounter', image)

        ch  =  cv2.waitKey(1)
        if(ch == ord('q') or ch == ord('Q')):break
        if(ch == ord('r') or ch == ord('R')):count=0
    
    cap.release()
    cv2.destroyAllWindows()