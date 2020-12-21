import cv2

class GenRep:

    def representative(self,pose_list:list):
        arr=[sum(i.diff.values()) for i in pose_list]
        mean_arr=sum(arr)/len(arr)
        arr=[i-mean_arr for i in arr]
        ind=arr.index(min(arr))
        return pose_list[ind]
    
    def getMaxDevPose(self,representatives:list):
        arr=[sum(i.diff.values()) for i in representatives]
        ind=arr.index(max(arr))
        return representatives[ind]

    def divider(self,data:list, phases:list):
        div_data=[[] for i in range(len(phases))]
        prev_curr_phase=data[0].curr_phase
        start_temp=0
        counter=0
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
        div_data=[self.getMaxDevPose([self.representative(j) for j in i]) for i in div_data]
        return div_data

    def dist2pts(self,a,b):
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

    def plotAngles(self,obj):
        img=obj.image
        pts=obj.reduced
        angles=obj.angles
        font=cv2.FONT_HERSHEY_SIMPLEX
        for i in angles.keys():
            print(angles[i].angle)
        for i in angles.keys():
            ang=angles[i].angle
            pt1=(int(pts[i[0]].y),int(pts[i[0]].x))
            pt2=(int(pts[i[1]].y),int(pts[i[1]].x))
            pt3=(int(pts[i[2]].y),int(pts[i[2]].x))
            img=cv2.arrowedLine(img,pt2,pt1,(0,255,0),4)
            img=cv2.arrowedLine(img,pt2,pt3,(0,255,0),4)
            radius=int(self.dist2pts(pt1,pt2)+self.dist2pts(pt2,pt3))//20
            img=cv2.circle(img,pt2,radius,(0,255,0),2)
            img=cv2.putText(img,"{:.1f}".format(ang), (pt2[0]+radius+5,pt2[1]), font, 1.5, (255, 0, 0), 5)
        return img

    def generate_report(self, div_data, phases):
        for i in div_data:
            img=self.plotAngles(i)
            cv2.imshow("plotted angles",img)
            cv2.waitKey()


    def __init__(self,data:list, phases:list):
        div_data=self.divider(data,phases)
        div_data=self.reducer(div_data)
        self.report=self.generate_report(div_data,phases)