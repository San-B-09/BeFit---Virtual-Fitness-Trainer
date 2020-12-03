import tensorflow as tf
import cv2
import posenet

# scale_factor=1
# model_name=101

# file_name="references\\squats\\frame_0_delay-0.3s.jpg"

def getDet(file_name,model_name=101,scale_factor=1):
    sess=tf.Session()
    model_cfg, model_outputs = posenet.load_model(model_name, sess)
    output_stride = model_cfg['output_stride']

    cap = cv2.VideoCapture(file_name)

    input_image, display_image, output_scale = posenet.read_cap(
            cap, scale_factor=scale_factor, output_stride=output_stride)

    heatmaps_result,offsets_result,displacement_fwd_result,displacement_bwd_result=sess.run(
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
        min_pose_score=0)
    keypoint_coords *= output_scale
    lst=[]
    for i in range(17):
        lst.append([keypoint_coords[0][i][0],keypoint_coords[0][i][1],keypoint_scores[0][i]])
    return lst

def getFastDet(cap,scale_factor,output_stride,sess,model_outputs,conf):
    input_image, display_image, output_scale = posenet.read_cap(
            cap, scale_factor=scale_factor, output_stride=output_stride)

    heatmaps_result,offsets_result,displacement_fwd_result,displacement_bwd_result=sess.run(
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
        min_pose_score=0)
    keypoint_coords *= output_scale

    image = posenet.draw_skel_and_kp(
            display_image, pose_scores, keypoint_scores, keypoint_coords,
            min_pose_score=0, min_part_score=conf)
    lst=[]
    for i in range(keypoint_coords.shape[1]):
        lst.append([keypoint_coords[0][i][0],keypoint_coords[0][i][1],keypoint_scores[0][i]])
    return lst,image
