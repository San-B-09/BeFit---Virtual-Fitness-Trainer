import cv2
def write(image,s,curr_phase,count,total_phases):
    img_h,img_w,_=image.shape
    y=30
    font=cv2.FONT_HERSHEY_SIMPLEX
    if s.isOkay:
        image  =  cv2.putText(image, "READY", (10, img_h//5), font, 1.5, (0, 255, 0), 4)
        image  =  cv2.putText(image, str(curr_phase), (10, 3*img_h//5), font, 1.5, (80, 4, 235), 3)
    else:
        image  =  cv2.putText(image, "NOT READY", (10,img_h//5), font, 1.5, (0, 0, 255), 4)
    
    image  =  cv2.putText(image, "Total phases "+str(total_phases), (10, 2*img_h//5), font, .5, (255, 0, 0), 1)
    image  =  cv2.putText(image, "COUNT: "+str(count), (10, img_h-y), font, 1.5, (255, 0, 0), 5)

    return image