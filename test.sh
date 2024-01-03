



#############################################################
# config='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/configs/1.instance_seg/HEK293T_ms_dct_base-maxvit_cascade_mask_rcnn_r50_fpn_1x_coco.py'
# model='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/2.hek293t_dct_ms8442_v3_base_640_maxvit_cascade_mask_rcnn_r50_fpn_1x_coco/epoch_240.pth'


############################################################# cascade_mask_rcnn 
# config='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/configs/1.instance_seg/1.LIVECell_cascade_mask_rcnn_r50_fpn_1x_coco.py'
# model='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/1.LIVECell_cascade_mask_rcnn_r50_fpn_1x_coco/epoch_140.pth'
# model='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/1.LIVECell_v1_cascade_mask_rcnn_r50_fpn_1x_coco/epoch_140.pth'
# model='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/1.LIVECell_v2_cascade_mask_rcnn_r50_fpn_1x_coco/epoch_40.pth'


# model='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/1.LIVECell_v1_cascade_mask_rcnn_r50_fpn_1x_coco/epoch_70.pth'



############################################################# ms_base-maxvit_cascade_mask_rcnn
config='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/configs/1.instance_seg/1.LIVECell_ms_base-maxvit_cascade_mask_rcnn_r50_fpn_1x_coco.py'
model='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/1.LIVECell_ms_base-maxvit_cascade_mask_rcnn_r50_fpn_1x_coco/epoch_140.pth'


############################################################# cascade_mask_rcnn 


# config='/home/jinlongli/1.Detection_Set/Instance_mmdet/MM/mmdetection/configs/1.instance_seg/HEK293T_ms_dct_base-maxvit_cascade_mask_rcnn_r50_fpn_1x_coco.py'
# model='/home/jinlongli/1.Detection_Set/Instance_mmdet/MM/mmdetection/work_dirs/1.Instance_seg_model/2.hek293t_dct_ms8442_v3_base_640_maxvit_cascade_mask_rcnn_r50_fpn_1x_coco/epoch_240.pth'


# config='/home/jinlongli/1.Detection_Set/Instance_mmdet/MM/mmdetection/configs/1.instance_seg/HEK293T_ms_dct_base-maxvit_cascade_mask_rcnn_r50_fpn_1x_coco.py'

# model='/home/jinlongli/1.Detection_Set/Instance_mmdet/MM/mmdetection/work_dirs/1.Instance_seg_model/2.hek293t_dct_ms8442_v3_base_640_maxvit_cascade_mask_rcnn_r50_fpn_1x_coco/epoch_239.pth'



# output='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/vis_LIVECell_2.5'
output='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/vis_LIVECell_vis'
# output='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/vis_testing'


if [ ! -d $output ]; then
    mkdir -p $output
fi


file=result.pkl

# output_result="${output}/${file}"
output_result='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/vis_LIVECell_vis/result41.pkl'





CUDA_VISIBLE_DEVICES=0 python3 tools/test.py \
    $config \
    $model  \
    --eval bbox segm  \
#     --out $output_result 
    # --show-dir $output 
    
    # [--show]


# CUDA_VISIBLE_DEVICES=1 python tools/misc/browse_dataset.py \
#         $config \
#         --output-dir  $output \
#         --not-show



#!/bin/bash

# A='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/1.LIVECell_cascade_mask_rcnn_r50_fpn_1x_coco/'
# A='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/1.LIVECell_v2_cascade_mask_rcnn_r50_fpn_1x_coco/'
# model_name='epoch_'
# max_number=40
# start=1

# # for ((i=start; i<=max_number; i++)); do
# for ((i=start; i<=max_number; i+=1)); do
#     model="${A}${model_name}${i}.pth"
#     echo -e "Model Path $i: $model\n"
#     # 在这里可以添加你想要执行的操作，比如训练模型等
#     CUDA_VISIBLE_DEVICES=0 python3 tools/test.py \
#         $config \
#         $model  \
#         --eval bbox segm  
# done
