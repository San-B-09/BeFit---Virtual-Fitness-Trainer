import tensorflow as tf
import cv2
import posenet
from lucas import poseEst
from lucas import lucas
import time

sess,model_cfg,model_outputs,output_stride=poseEst.load_model()

cap = cv2.VideoCapture(0)

count=0
gap=2

total_time=0
start=None
while True:

    input_image, display_image, output_scale = posenet.read_cap(
        cap, scale_factor=1, output_stride=output_stride)
    
    if count%gap==0:
        if start!=None:
            fps="FPS:{:.3f}".format(gap/(time.time()-start))
        else:
            fps="FPS:N/A"
        start=time.time()
        pose_score,points,scores=poseEst.pose_est(sess,input_image,model_outputs,output_stride,output_scale)
        last_image=display_image
    else:
        try:
            points=lucas.getDet(last_image,display_image,points)
        except:
            count=0
            continue
    count+=1
    try:
        image = posenet.draw_skel_and_kp(
            display_image, pose_score, scores, points,
            min_pose_score=0, min_part_score=0.1)
    except:
        continue

    total_time+=(time.time()-start)

    # print("Execution time:",time.time()-start)
    image  =  cv2.putText(image,fps,(20, 40),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
    cv2.imshow('lucas', image)


    ch  =  cv2.waitKey(1)
    if(ch == ord('q') or ch == ord('Q')):break

cap.release()
cv2.destroyAllWindows()