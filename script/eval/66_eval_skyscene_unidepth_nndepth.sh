#!/usr/bin/env bash
set -e
set -x

subfolder=${1:-"Unidepth/eval_after_command_run"}

# --prediction_dir /mnt/data/bientd/NDDepth/assets/raw_max_depth_10/raw_max_depth_10 \
python eval_unidepth_nndepth.py \
    --base_data_dir "" \
    --dataset_config config/dataset/data_skyscenes_test.yaml \
    --prediction_dir /mnt/data/bientd/UniDepth/Town07 \
    --output_dir output/${subfolder}/skyscenes_test/eval_metric \
    --alignment least_square \