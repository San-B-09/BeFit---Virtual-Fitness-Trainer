import tensorflow as tf
import cv2

import posenet
from posenet.singleImageDet import getFastDet

from pose.getAppropriateObject import getObject

from excAnalyser.getPhaseAndDeviation import getPhase
from excAnalyser.loadRef import loadReference


cam_id = 0
cam_width = 1080
cam_height = 720
scale_factor = 0.7125
model_name = 101
conf=0.2

with tf.Session() as sess:

    model_cfg, model_outputs  =  posenet.load_model(model_name, sess)
    output_stride  =  model_cfg['output_stride']

    excercise = input("Name of excercise: ")
    phases=loadReference(excercise,conf)

    cap  =  cv2.VideoCapture(cam_id)
    cap.set(3, cam_width)
    cap.set(4, cam_height)

    while True:
        lst, image = getFastDet(cap, scale_factor, output_stride, sess, model_outputs)

        s = getObject(excercise, lst, conf)
        
        y0, dy = 20, 20
        for i, line in enumerate(s.reduced.keys()):
            y = y0 + i*dy
            o = s.reduced[line]
            line = [line, str(int(o.x)), str(int(o.y)), str(int(o.conf*100))]
            line = "|".join([k.ljust(15, ' ') for k in line])
            image = cv2.putText(image, line, (10, y), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 1)

        if s.isOkay:tmp = "READY"
        else:tmp = "NOT READY"
        image  =  cv2.putText(image, tmp, (10, y+20), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 0), 2)
        image  =  cv2.putText(image, "Total phases "+str(len(phases)), (10, y+40), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 0), 2)
        if s.isOkay:
            curr_phase,diff=getPhase(s,phases)
            image  =  cv2.putText(image, "Current phase "+str(curr_phase), (10, y+60), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 0), 2)
        cv2.imshow('RepCounter', image)
        ch  =  cv2.waitKey(1)
        if(ch == ord('q') or ch == ord('Q')):break
    
    cap.release()
    cv2.destroyAllWindows()