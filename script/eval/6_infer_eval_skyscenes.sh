#!/usr/bin/env bash
set -e
set -x

bash script/eval/61_infer_skyscenes.sh
bash script/eval/62_eval_skyscenes.sh