


#conda activate openmmlab1

########____________HEK293T____________________########################



#################________________________________________________________________________________________________________________________


###LIVECell########################



################___________MoNuSeg___________________#########################




#################________________________________________________________________________________________________________________________

# id=0

# id=1

# id=2

#id=3

# id=4

# id=5

# id=6

id=7



############################# cascade_mask_rcnn
# config='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/configs/1.instance_seg/1.LIVECell_cascade_mask_rcnn_r50_fpn_1x_coco.py'


#######################  ms_base-maxvit_cascade_mask_rcnn
# config='/home/jinlongli/1.Detection_Set/Instance_mmdet/MM/mmdetection/configs/1.instance_seg/1.LIVECell_ms_base-maxvit_cascade_mask_rcnn_r50_fpn_1x_coco.py'

config='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/configs/1.instance_seg/1.LIVECell_base-maxvit_cascade_mask_rcnn_r50_fpn_1x_coco.py'


# config='/home/jinlongli/1.Detection_Set/Instance_mmdet/MM/mmdetection/configs/1.instance_seg/1.LIVECell_dct_base-maxvit_cascade_mask_rcnn_r50_fpn_1x_coco.py'


# config='/home/jinlongli/1.Detection_Set/Instance_mmdet/MM/mmdetection/configs/1.instance_seg/HEK293T_ms_dct_base-maxvit_cascade_mask_rcnn_r50_fpn_1x_coco.py'

# config='/home/jinlongli/1.Detection_Set/Instance_mmdet/MM/mmdetection/configs/1.instance_seg/LIVECell_ms_dct_base-maxvit_cascade_mask_rcnn_r50_fpn_1x_coco.py'

# export CUDA_VISIBLE_DEVICES=4

# CUDA_VISIBLE_DEVICES=4 tools/dist_train.sh $config  1

# CUDA_VISIBLE_DEVICES=$id python3 tools/train.py  $config



# CUDA_LAUNCH_BLOCKING=1  python3 tools/train.py $config --gpu-id $id

# CUDA_VISIBLE_DEVICES=4,5  ./tools/dist_train.sh $config 2




CUDA_VISIBLE_DEVICES=1,2,3,4,5 tools/dist_train.sh $config  5
