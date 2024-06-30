#!/usr/bin/env bash
set -e
set -x

# subfolder=${1:-"Skyscence_all_town/eval_after_command_run"}

# python eval_skyscene.py \
#     --base_data_dir "" \
#     --dataset_config config/dataset/data_skyscenes_test.yaml \
#     --prediction_dir /mnt/data/bientd/Marigold/output/Skyscence_all_town/depth_npy \
#     --output_dir output/${subfolder}/skyscenes_test/eval_metric \
#     --alignment least_square \


subfolder=${1:-"Skyscence_all_town_finetune_v2/eval"}

python eval.py \
    --base_data_dir "" \
    --dataset_config config/dataset/data_skyscenes_test.yaml \
    --prediction_dir output/${subfolder}/skyscenes_test/prediction \
    --output_dir output/${subfolder}/skyscenes_test/eval_metric \
    --alignment least_square \