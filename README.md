# BeFit - Virtual Fitness Trainer
BeFit a virtual fitness trainer is your exercise companion, that helps you perform exercise posture correctly and also keeps the track of your repetition count.
Currently the repository holds the system built for 6 different exercises in total that are: Squats, Push-up, Sit-up, Bicep press, Dumbell lateral raises and Dumbell upper head.

## Installation Guide
pip install -r requirements.txt

python setup.py build
python setup.py install

python prepReference.py
(optional)

python myrun.py

## Brief System Overview

The complete system is based on two stages. The first one being 2D human body tracking and second one is the proposed statistical model for processing extracted coordinates. The 2D human body tracking uses [PoseNet](https://github.com/tensorflow/tfjs-models/tree/master/posenet) along with lucas kanade's algorithm to enhance the frame rate and extract 2D body keypoints. Later these keypoints are passes through a statistical model for repetation count and report generation for wrong posture. 

Following flow diagram describe brief overview:
![Overview Image](https://github.com/San-B-09/BeFit---Virtual-Fitness-Trainer/blob/master/Images/brief%20overview.png)


## Enhancement of 2D Body Tracking using Lucas Kanade's Algorithm
The 2D body tracking is achieved with State-of-the-art model [PoseNet](https://github.com/tensorflow/tfjs-models/tree/master/posenet) extending with the Lucas Kanade's algorithm on alternate frames to achieve an higher average frame rate. Use of Lucas Kanade's algorithm with a gap of 3 frames, enhanced frame rate from ~4.00 fps to ~13.8 fps, maintaining the body tracking accuracy. 

Following flow diagram displays the architecture of complete 2D body tracking system used here:
![Body Tracking Architecture Image](https://github.com/San-B-09/BeFit---Virtual-Fitness-Trainer/blob/master/Images/overall%20system%20architecture.png)

## Statistical Model
The statistical model, processes the body coordinated extracted from 2D body tracking system to give the repitation count and posture correction report. Following are the algorithmic steps used in statistical model:
* **Step 1:** Take the stream of 2D body coordinates from 2D body tracking model for the current frame.
* **Step 2:** Droping all the unnecessary key points, store the essential key points in a dictionary. Also, check for all necessary key points, if the confidence of all the points is above a threshold. **(∀x, Confidence of x >= Threshold Confidence, where x is the necessary key point)**
* **Step 3:** Calculate the angles using filtered key points from previous step using following equation.\
**a = (p1.x -p2.x, p1.y – p2.y)\
b = (p1.x -p3.x, p1.y – p3.y)\
θ=  arccos((a.b)/(|a|.|b|))\
where p1, p2, p3 are 3 key points. i.e., a and b being two vectors and θ is the angle between those two vectors.**
* **Step 4:** Calculate the deviation of angles with the reference pose angle and classify current posture into one of the reference phases.
* **Step 5:** Furthermore, store the body coordinates, calculated angles, and current phase for posture correction suggestions.
* **Step 6:** Increment the repetition counter using the stream of current phases. i.e., a phase pattern like 0,0,0,1,1,2,3,3,2,2,2,1,0 means to increment the counter by 1.


## Results
The repetition counter mechanism works on the basis of the obtained phases stream. The phase list is initially empty, and after each phase classification, the corresponding pose is added to the phase list. Each updating in the list, call the function updateCounter to check whether to update the counter or not. 

Using the stored body coordinate angles, the most deviated frame per phase is selected from each phase. Moreover, these frames are compared with reference frames and the incorrect angles are marked in red color. 

Following figure shows the posture correction report:
![Result report](https://github.com/San-B-09/BeFit---Virtual-Fitness-Trainer/blob/master/Images/posture%20correction%20report.png)

**Following video dipicts the complete output of the system with explaination -> https://youtu.be/isVScThUCa0**
