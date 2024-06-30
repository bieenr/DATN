#!/usr/bin/env bash
set -e
set -x

# Use specified checkpoint path, otherwise, default value
# ckpt=${1:-"prs-eth/marigold-v1-0"}
ckpt=${1:-"/mnt/data/bientd/Marigold/checkpoint/marigold-v1-0"}
subfolder=${2:-"eval"}

python infer.py  \
    --checkpoint $ckpt \
    --seed 1234 \
    --base_data_dir '' \
    --denoise_steps 50 \
    --ensemble_size 10 \
    --processing_res 0 \
    --dataset_config config/dataset/data_skyscenes_test.yaml \
    --output_dir output/${subfolder}/skyscenes_test/prediction \
