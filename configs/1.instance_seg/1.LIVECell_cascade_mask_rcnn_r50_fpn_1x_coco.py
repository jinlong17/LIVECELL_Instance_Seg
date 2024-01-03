model = dict(
    type='CascadeRCNN',
    backbone=dict(
        type='ResNet',
        depth=50,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),
        norm_eval=True,
        style='pytorch',
        init_cfg=dict(type='Pretrained', checkpoint='torchvision://resnet50')),
    neck=dict(
        type='FPN',
        in_channels=[256, 512, 1024, 2048],
        out_channels=256,
        num_outs=5),
    rpn_head=dict(
        type='RPNHead',
        in_channels=256,
        feat_channels=256,
        anchor_generator=dict(
            type='AnchorGenerator',
            scales=[8],
            # ratios=[0.5, 1.0, 2.0],
            ratios=[0.25, 0.5, 1.0, 2.0, 4.0],
            strides=[4, 8, 16, 32, 64]),
        bbox_coder=dict(
            type='DeltaXYWHBBoxCoder',
            target_means=[0.0, 0.0, 0.0, 0.0],
            target_stds=[1.0, 1.0, 1.0, 1.0]),
        loss_cls=dict(
            type='CrossEntropyLoss', use_sigmoid=True, loss_weight=1.0),
        loss_bbox=dict(
            type='SmoothL1Loss', beta=0.1111111111111111, loss_weight=1.0)),
    roi_head=dict(
        type='CascadeRoIHead',
        num_stages=3,
        stage_loss_weights=[1, 0.5, 0.25],
        bbox_roi_extractor=dict(
            type='SingleRoIExtractor',
            roi_layer=dict(type='RoIAlign', output_size=7, sampling_ratio=0),
            out_channels=256,
            featmap_strides=[4, 8, 16, 32]),
        bbox_head=[
            dict(
                type='Shared2FCBBoxHead',
                in_channels=256,
                fc_out_channels=1024,
                roi_feat_size=7,
                num_classes=1,#80
                bbox_coder=dict(
                    type='DeltaXYWHBBoxCoder',
                    target_means=[0.0, 0.0, 0.0, 0.0],
                    target_stds=[0.1, 0.1, 0.2, 0.2]),
                reg_class_agnostic=True,
                loss_cls=dict(
                    type='CrossEntropyLoss',
                    use_sigmoid=False,
                    loss_weight=1.0),
                loss_bbox=dict(type='SmoothL1Loss', beta=1.0,
                               loss_weight=1.0)),
            dict(
                type='Shared2FCBBoxHead',
                in_channels=256,
                fc_out_channels=1024,
                roi_feat_size=7,
                num_classes=1,
                bbox_coder=dict(
                    type='DeltaXYWHBBoxCoder',
                    target_means=[0.0, 0.0, 0.0, 0.0],
                    target_stds=[0.05, 0.05, 0.1, 0.1]),
                reg_class_agnostic=True,
                loss_cls=dict(
                    type='CrossEntropyLoss',
                    use_sigmoid=False,
                    loss_weight=1.0),
                loss_bbox=dict(type='SmoothL1Loss', beta=1.0,
                               loss_weight=1.0)),
            dict(
                type='Shared2FCBBoxHead',
                in_channels=256,
                fc_out_channels=1024,
                roi_feat_size=7,
                num_classes=1,
                bbox_coder=dict(
                    type='DeltaXYWHBBoxCoder',
                    target_means=[0.0, 0.0, 0.0, 0.0],
                    target_stds=[0.033, 0.033, 0.067, 0.067]),
                reg_class_agnostic=True,
                loss_cls=dict(
                    type='CrossEntropyLoss',
                    use_sigmoid=False,
                    loss_weight=1.0),
                loss_bbox=dict(type='SmoothL1Loss', beta=1.0, loss_weight=1.0))
        ],
        mask_roi_extractor=dict(
            type='SingleRoIExtractor',
            roi_layer=dict(type='RoIAlign', output_size=14, sampling_ratio=0),
            out_channels=256,
            featmap_strides=[4, 8, 16, 32]),
        mask_head=dict(
            type='FCNMaskHead',
            num_convs=4,
            in_channels=256,
            conv_out_channels=256,
            num_classes=1,
            loss_mask=dict(
                type='CrossEntropyLoss', use_mask=True, loss_weight=1.0))),
    train_cfg=dict(
        rpn=dict(
            assigner=dict(
                type='MaxIoUAssigner',
                pos_iou_thr=0.7,
                neg_iou_thr=0.3,
                min_pos_iou=0.3,
                match_low_quality=True,
                ignore_iof_thr=-1),
            sampler=dict(
                type='RandomSampler',
                num=256,
                pos_fraction=0.5,
                neg_pos_ub=-1,
                add_gt_as_proposals=False),
            allowed_border=0,
            pos_weight=-1,
            debug=False),
        rpn_proposal=dict(
            nms_pre=12000,#2000
            max_per_img=6000,#2000
            nms=dict(type='nms', iou_threshold=0.7),
            min_bbox_size=0),
        rcnn=[
            dict(
                assigner=dict(
                    type='MaxIoUAssigner',
                    pos_iou_thr=0.5,
                    neg_iou_thr=0.5,
                    min_pos_iou=0.5,
                    match_low_quality=False,
                    ignore_iof_thr=-1),
                sampler=dict(
                    type='RandomSampler',
                    num=512,
                    pos_fraction=0.25,
                    neg_pos_ub=-1,
                    add_gt_as_proposals=True),
                mask_size=28,
                pos_weight=-1,
                debug=False),
            dict(
                assigner=dict(
                    type='MaxIoUAssigner',
                    pos_iou_thr=0.6,
                    neg_iou_thr=0.6,
                    min_pos_iou=0.6,
                    match_low_quality=False,
                    ignore_iof_thr=-1),
                sampler=dict(
                    type='RandomSampler',
                    num=512,
                    pos_fraction=0.25,
                    neg_pos_ub=-1,
                    add_gt_as_proposals=True),
                mask_size=28,
                pos_weight=-1,
                debug=False),
            dict(
                assigner=dict(
                    type='MaxIoUAssigner',
                    pos_iou_thr=0.7,
                    neg_iou_thr=0.7,
                    min_pos_iou=0.7,
                    match_low_quality=False,
                    ignore_iof_thr=-1),
                sampler=dict(
                    type='RandomSampler',
                    num=512,
                    pos_fraction=0.25,
                    neg_pos_ub=-1,
                    add_gt_as_proposals=True),
                mask_size=28,
                pos_weight=-1,
                debug=False)
        ]),
    test_cfg=dict(
        rpn=dict(
            nms_pre=80000,
            max_per_img=20000,
            nms=dict(type='nms', iou_threshold=0.90),#0.7
            min_bbox_size=0),#0
        rcnn=dict(
            score_thr=0.05,##0.05
            nms=dict(type='nms', iou_threshold=0.5),#0.5
            max_per_img=20000,
            mask_thr_binary=0.5)))#0.5


dataset_type = 'CocoDataset'
data_root = '/home/jinlongli/LIVECell_dataset/LIVECell/'


metainfo = {
    'classes': ('cell', ),
    'palette': [
        (220, 20, 60),
    ]
}

classes=('cell',)

train_ann_file='/home/jinlongli/LIVECell_dataset/LIVECell/livecell_coco_train.json'
train_img_path='/home/jinlongli/LIVECell_dataset/LIVECell/images/livecell_train_val_images'
val_ann_file='/home/jinlongli/LIVECell_dataset/LIVECell/livecell_coco_val.json'
val_img_path='/home/jinlongli/LIVECell_dataset/LIVECell/images/livecell_test_images'
test_ann_file='/home/jinlongli/LIVECell_dataset/LIVECell/livecell_coco_test.json'
test_img_path='/home/jinlongli/LIVECell_dataset/LIVECell/images/livecell_test_images'

# train_ann_file='/home/jinlongli/LIVECell_dataset/LIVECell/livecell_coco_train.json'
# train_img_path='/home/jinlongli/LIVECell_dataset/LIVECell/images/livecell_train_val_images'
# train_ann_file='/home/jinlongli/LIVECell_dataset/LIVECell/livecell_coco_test.json'
# train_img_path='/home/jinlongli/LIVECell_dataset/LIVECell/images/livecell_test_images'

# load_from='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/1.LIVECell_cascade_mask_rcnn_r50_fpn_1x_coco/epoch_140.pth'
load_from ='/home/jinlongli/1.Detection_Set/LIVE_Seg/MM/mmdetection/work_dirs/1.Instance_seg_model/1.LIVECell_v1_cascade_mask_rcnn_r50_fpn_1x_coco/epoch_140.pth'
work_dir = './work_dirs/1.Instance_seg_model/1.LIVECell_v2_cascade_mask_rcnn_r50_fpn_1x_coco'
# auto_resume = False
gpu_ids = [0]

max_epochs=40
samples_per_gpu=2
img_scale=(960, 960)
val_interval=40
interval=1

img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
    dict(type='Resize', img_scale=img_scale, keep_ratio=False),
    # dict(
    #     type='Resize',
    #     img_scale=[
    #         (1333, 440), (1333, 480),
    #         (1333, 520), (1333,580),
    #         (1333, 620)],
    #     multiscale_mode='value',
    #     keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(
        type='Normalize',
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375],
        to_rgb=True),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks'])
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    # dict(
    #     type='MultiScaleFlipAug',
    #     img_scale=img_scale,
    #     flip=False,
    #     transforms=[
    #         dict(type='Resize', keep_ratio=True),
    #         dict(type='RandomFlip'),
    #         dict(
    #             type='Normalize',
    #             mean=[123.675, 116.28, 103.53],
    #             std=[58.395, 57.12, 57.375],
    #             to_rgb=True),
    #         dict(type='Pad', size_divisor=32),
    #         dict(type='ImageToTensor', keys=['img']),
    #         dict(type='Collect', keys=['img'])
    #     ])
    dict(type='Resize', img_scale=img_scale,keep_ratio=False),
    dict(
        type='Normalize',
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375],
        to_rgb=True),
    dict(type='Pad', size_divisor=32),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='Collect', keys=['img'])
    
]
data = dict(
    samples_per_gpu=samples_per_gpu,
    workers_per_gpu=4,
    train=dict(
        type='CocoDataset',
        # metainfo=metainfo,
        classes=classes,
        ann_file=train_ann_file,
        img_prefix=train_img_path,
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
            dict(type='Resize', img_scale=img_scale, keep_ratio=True),
            # dict(type='RandomFlip', flip_ratio=0.5),
            dict(type='RandomFlip', flip_ratio=0.5, direction='vertical'),
            dict(type='RandomFlip', flip_ratio=0.5, direction='horizontal'),
            dict(type='RandomFlip', flip_ratio=0.5, direction='diagonal'),
            
            dict(
                type='Normalize',
                mean=[123.675, 116.28, 103.53],
                std=[58.395, 57.12, 57.375],
                to_rgb=True),
            dict(type='Pad', size_divisor=32),
            dict(type='DefaultFormatBundle'),
            dict(
                type='Collect',
                keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks'])
        ]),
    val=dict(
        type='CocoDataset',
        # metainfo=metainfo,
        classes=classes,
        ann_file=test_ann_file,
        img_prefix=test_img_path,
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(
                type='MultiScaleFlipAug',
                img_scale=img_scale,
                flip=False,
                transforms=[
                    dict(type='Resize', keep_ratio=True),
                    dict(type='RandomFlip'),
                    dict(
                        type='Normalize',
                        mean=[123.675, 116.28, 103.53],
                        std=[58.395, 57.12, 57.375],
                        to_rgb=True),
                    dict(type='Pad', size_divisor=32),
                    dict(type='ImageToTensor', keys=['img']),
                    dict(type='Collect', keys=['img'])
                ])
        ]),
    test=dict(
        type='CocoDataset',
        # metainfo=metainfo,
        classes=classes,
        ann_file=test_ann_file,
        img_prefix=test_img_path,
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(
                type='MultiScaleFlipAug',
                img_scale=img_scale,
                flip=False,
                transforms=[
                    dict(type='Resize', keep_ratio=True),
                    dict(type='RandomFlip'),
                    dict(
                        type='Normalize',
                        mean=[123.675, 116.28, 103.53],
                        std=[58.395, 57.12, 57.375],
                        to_rgb=True),
                    dict(type='Pad', size_divisor=32),
                    dict(type='ImageToTensor', keys=['img']),
                    dict(type='Collect', keys=['img'])
                ])
        ]))
evaluation = dict(metric=['segm', 'bbox'])
optimizer = dict(type='SGD', lr=0.002, momentum=0.9, weight_decay=0.0001)#0.02
optimizer_config = dict(grad_clip=None)
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.0001,
    # step=[8, 11]
    step=[20, 40, 60]
    # step=[80,100]
    )
runner = dict(type='EpochBasedRunner', max_epochs=max_epochs)
checkpoint_config = dict(interval=interval)
log_config = dict(interval=50, hooks=[dict(type='TextLoggerHook')])
custom_hooks = [dict(type='NumClassCheckHook')]
dist_params = dict(backend='nccl')
log_level = 'INFO'
# load_from = None
resume_from = None
workflow = [('train', 1)]
opencv_num_threads = 0
mp_start_method = 'fork'
auto_scale_lr = dict(enable=False, base_batch_size=16)
evaluation = dict(interval=val_interval)