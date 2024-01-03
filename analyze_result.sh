




####################################
# CONFIG='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/configs/1.instance_seg/HEK293T_ms_dct_base-maxvit_cascade_mask_rcnn_r50_fpn_1x_coco.py'
# PREDICTION_PATH='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/vis_testing/result.pkl'


############################################################# cascade_mask_rcnn 
CONFIG='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/configs/1.instance_seg/1.LIVECell_cascade_mask_rcnn_r50_fpn_1x_coco.py'
PREDICTION_PATH='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/vis_LIVECell_vis/result23.pkl'


SHOW_DIR='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/vis_LIVECell_23'


if [ ! -d $SHOW_DIR ]; then
    mkdir -p $SHOW_DIR
fi



CUDA_VISIBLE_DEVICES=1 python tools/analysis_tools/analyze_results.py \
      $CONFIG \
      $PREDICTION_PATH \
      $SHOW_DIR \
      --topk 500 \
    #   [--show-score-thr ${SHOW_SCORE_THR}] \
    #   [--cfg-options ${CFG_OPTIONS}]