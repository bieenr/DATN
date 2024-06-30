#!/usr/bin/env bash
set -e
set -x

subfolder=${1:-"Skyscene_pretrain_add_trash_prompt_0/eval_after_command_run"}

python eval_skyscene.py \
    --base_data_dir "" \
    --dataset_config config/dataset/data_skyscenes_test.yaml \
    --prediction_dir /mnt/data/bientd/Marigold/output/Skyscene_pretrain_add_trash_prompt_0/depth_npy \
    --output_dir output/${subfolder}/skyscenes_test/eval_metric \
    --alignment least_square \