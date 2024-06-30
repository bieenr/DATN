#!/usr/bin/env bash
set -e
set -x

subfolder=${1:-"eval"}

python eval.py \
    --base_data_dir "" \
    --dataset_config config/dataset/data_skyscenes_test.yaml \
    --prediction_dir output/${subfolder}/skyscenes_test/prediction \
    --output_dir output/${subfolder}/skyscenes_test/eval_metric \
    # --alignment least_square \