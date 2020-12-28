import cv2
import numpy as np

class GenRep:

    def representative(self,pose_list:list):
        arr=[sum(i.diff.values()) for i in pose_list]
        mean_arr=sum(arr)/len(arr)
        arr=[i-mean_arr for i in arr]
        ind=arr.index(min(arr))
        return pose_list[ind]

    def getMinDevPose(self,representatives:list):
        arr=[sum(i.diff.values()) for i in representatives]
        ind=arr.index(min(arr))
        return representatives[ind]

    def getMaxDevPose(self,representatives:list):
        arr=[sum(i.diff.values()) for i in representatives]
        ind=arr.index(max(arr))
        return representatives[ind]

    def divider(self,data:list, phases:list):
        div_data=[[] for i in range(len(phases))]
        prev_curr_phase=data[0].curr_phase
        start_temp=0
        counter=0
        max_count=data[-1].count
        data=[i for i in data if i.count!=0 and i.count!=max_count]
        for i in data[1:]:
            counter+=1
            if i.curr_phase==prev_curr_phase:
                pass
            else:
                div_data[prev_curr_phase].append(data[start_temp:counter])
                prev_curr_phase=i.curr_phase
                start_temp=counter
        return div_data

    def reducer(self,div_data):
        div_data=[self.getMaxDevPose([self.getMinDevPose(j) for j in i]) for i in div_data]
        return div_data

    def dist2pts(self,a,b):
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

    def plotAngles(self,obj,target=300):
        img=obj.image
        pts=obj.reduced
        angles=obj.angles
        font=cv2.FONT_HERSHEY_SIMPLEX
        for i in angles.keys():
            ang=angles[i].angle
            pt1=(int(pts[i[0]].y),int(pts[i[0]].x))
            pt2=(int(pts[i[1]].y),int(pts[i[1]].x))
            pt3=(int(pts[i[2]].y),int(pts[i[2]].x))
            img=cv2.arrowedLine(img,pt2,pt1,(0,255,0),4)
            img=cv2.arrowedLine(img,pt2,pt3,(0,255,0),4)
            radius=int(self.dist2pts(pt1,pt2)+self.dist2pts(pt2,pt3))//25
            img=cv2.circle(img,pt2,radius,(0,255,0),1)
            if angles[i].okay:
                img=cv2.putText(img,"{:.1f}".format(ang), (pt2[0]+radius+5,pt2[1]), font, 1, (0, 255, 0), 2)
            else:
                img=cv2.putText(img,"{:.1f}".format(ang), (pt2[0]+radius+5,pt2[1]), font, 1, (0, 0, 255), 2)
        target_size=int((img.shape[1]/img.shape[0])*target)
        img=cv2.resize(img,(target_size,target))
        return img

    def generate_report(self, div_data, phases):
        for i in range(len(phases)):
            target=400
            cv2.imshow("original image",div_data[i].image)
            cv2.waitKey()
            img=self.plotAngles(div_data[i],target)
            ref=self.plotAngles(phases[i],target)
            concat = np.concatenate((img, ref), axis=1)
            cv2.imshow("plotted angles",concat)
            cv2.waitKey()


    def __init__(self,data:list, phases:list):
        div_data=self.divider(data,phases)
        div_data=self.reducer(div_data)
        self.report=self.generate_report(div_data,phases)