#!/usr/bin/env bash
set -e
set -x

bash script/eval/64_infer_skyscenes_pretrain.sh
bash script/eval/63_eval_skyscenes_pretrain.sh