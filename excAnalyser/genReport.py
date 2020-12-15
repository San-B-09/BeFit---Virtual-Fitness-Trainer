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

    def __init__(self,data:list, phases:list):
        self.phases=phases
        div_data=self.divider(data,phases)
        div_data=self.reducer(div_data)
        for i in div_data:
            print(i.curr_phase,i.diff)