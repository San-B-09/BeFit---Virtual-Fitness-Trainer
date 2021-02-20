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
