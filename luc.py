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
win_s=10
numLevel=2

total_time=0
start=None
while True:

    input_image,display_image,output_scale = posenet.read_cap(
        cap,scale_factor=1,output_stride=output_stride)
    
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
            points=lucas.getDet(last_image,display_image,points,win_s,numLevel)
        except:
            count=0
            continue
    count+=1
    try:
        image = posenet.draw_skel_and_kp(
            display_image,pose_score,scores,points,
            min_pose_score=0,min_part_score=0.1)
    except:
        continue

    # total_time+=(time.time()-start)

    # print("Execution time:",time.time()-start)
    # print(image.shape)
    image[10:150,10:230]=[0,0,0]
    font=cv2.FONT_HERSHEY_SIMPLEX

    image  =  cv2.putText(image,fps,(20,40),font,1,(255,255,255),3)

    image  =  cv2.putText(image,"Gap:"+str(gap),(20,80),font,0.5,(255,255,255),1)
    image  =  cv2.putText(image,"[w:   s:  ]",(125,80),font,0.5,(255,255,255),1)
    image  =  cv2.arrowedLine(image, (155,80), (155,70), (255,255,255), 1, tipLength=0.5)
    image  =  cv2.arrowedLine(image, (190,70), (190,80), (255,255,255), 1, tipLength=0.5)

    image  =  cv2.putText(image,"Win:"+str(win_s),(20,100),font,0.5,(255,255,255),1)
    image  =  cv2.putText(image,"[d:   a:  ]",(125,100),font,0.5,(255,255,255),1)
    image  =  cv2.arrowedLine(image, (155,100), (155,90), (255,255,255), 1, tipLength=0.5)
    image  =  cv2.arrowedLine(image, (190,90), (190,100), (255,255,255), 1, tipLength=0.5)

    image  =  cv2.putText(image,"Levels:"+str(numLevel),(20,120),font,0.5,(255,255,255),1)
    image  =  cv2.putText(image,"[x:   z:  ]",(125,120),font,0.5,(255,255,255),1)
    image  =  cv2.arrowedLine(image, (155,120), (155,110), (255,255,255), 1, tipLength=0.5)
    image  =  cv2.arrowedLine(image, (190,110), (190,120), (255,255,255), 1, tipLength=0.5)

    cv2.imshow('lucas',image)


    ch  =  cv2.waitKey(1)

    if(ch == ord('q') or ch == ord('Q')):break
    elif ch==ord('w') or ch == ord('W'):gap+=1
    elif ch==ord('s') or ch == ord('S'):gap=max(1,gap-1)
    elif ch==ord('a') or ch == ord('A'):win_s=max(5,win_s-5)
    elif ch==ord('d') or ch == ord('D'):win_s+=5
    elif ch==ord('X') or ch == ord('x'):numLevel+=1
    elif ch==ord('Z') or ch == ord('z'):numLevel=max(1,numLevel-1)

cap.release()
cv2.destroyAllWindows()