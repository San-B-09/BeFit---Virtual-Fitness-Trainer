import tensorflow as tf
import cv2
import time
from excAnalyser.countReps import countRepetition
import posenet
import time

keyValues = ['Nose', 'Left eye', 'Right eye', 'Left ear', 'Right ear', 'Left shoulder',
             'Right shoulder', 'Left elbow', 'Right elbow', 'Left wrist', 'Right wrist',
             'Left hip', 'Right hip', 'Left knee', 'Right knee', 'Left ankle', 'Right ankle']

tolerance = 30
file_name=None
cam_id=0
cam_width=1280
cam_height=720
scale_factor=0.7125
model_name=101

with tf.Session() as sess:
    # Load the models
    model_cfg, model_outputs = posenet.load_model(model_name, sess)
    output_stride = model_cfg['output_stride']

    if file_name is not None: # Frame source, speicifed file or the specified(or default) live cam
        cap = cv2.VideoCapture(file_name)
    else:
        cap = cv2.VideoCapture(cam_id)
    cap.set(3, cam_width)
    cap.set(4, cam_height)
    previous_pose = '' # '' denotes it is empty, really fast checking!
    count = 0 # Stores the count of repetitions
    # A flag denoting change in state. 0 -> previous state is continuing, 1 -> state has changed
    flag = -1
    # Novel string stores a pair of bits for each of the 12 joints denoting whether the joint is moving up or down
    # when plotted in a graph against time, 1 denotes upward and 0 denotes downward curving of the graph. It is initialised
    # as '22' so that current_state wont ever be equal to the string we generate unless there is no movement out of tolerance
    current_state = [2,2]
    while True:
        # Get a frame, and get the model's prediction
        time1 = time.time()
        input_image, display_image, output_scale = posenet.read_cap(
            cap, scale_factor=scale_factor, output_stride=output_stride)
        heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = sess.run(
            model_outputs,
            feed_dict={'image:0': input_image}
        )
        pose_scores, keypoint_scores, keypoint_coords = posenet.decode_multi.decode_multiple_poses(
            heatmaps_result.squeeze(axis=0),
            offsets_result.squeeze(axis=0),
            displacement_fwd_result.squeeze(axis=0),
            displacement_bwd_result.squeeze(axis=0),
            output_stride=output_stride,
            max_pose_detections=1,
            min_pose_score=0.4)
        keypoint_coords *= output_scale # Normalising the output against the resolution

        if(isinstance(previous_pose, str)): # if previous_pose was not inialised, assign the current keypoints to it
            previous_pose = keypoint_coords
        
        text, previous_pose, current_state, flag = countRepetition(previous_pose, keypoint_coords, current_state, flag)

        if(flag == 1):
            count += 1
            flag = -1

        image = posenet.draw_skel_and_kp(
            display_image, pose_scores, keypoint_scores, keypoint_coords,
            min_pose_score=0.4, min_part_score=0.1)

        # OpenCV does not recognise the use of \n delimeter
        y0, dy = 20, 20
        for i, line in enumerate(text.split('\n')):
            y = y0 + i*dy
            image = cv2.putText(image, line, (10, y), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255),1)

        image = cv2.putText(image, 'Count: ' + str(count), (10, y+20), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,0,0),2)
        cv2.imshow('RepCounter', image)
        time2 = time.time()
        print(time2-time1)
        ch = cv2.waitKey(1)
        if(ch == ord('q') or ch == ord('Q')):
            break # Exit the loop on press of q or Q
        elif(ch == ord('r') or ch == ord('R')):
            count = 0
    
    cap.release()
    cv2.destroyAllWindows()