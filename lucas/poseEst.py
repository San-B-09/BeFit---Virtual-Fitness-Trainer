import tensorflow as tf
import cv2
import posenet

def load_model():
    sess=tf.Session()
    model_cfg, model_outputs = posenet.load_model(101, sess)
    output_stride = model_cfg['output_stride']
    return sess,model_cfg,model_outputs,output_stride

def pose_est(sess,input_image,model_outputs,output_stride,output_scale):
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
    return pose_scores,keypoint_coords,keypoint_scores