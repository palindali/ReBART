#!/bin/bash

DATA_DIR="data/dc2"
MODEL_PATH="outputs/bart-large_dc2"

python source/generate.py \
    --in_file ${DATA_DIR}/test.jsonl \
    --out_file ${MODEL_PATH}/test_bart_greedy.jsonl \
    --model_name_or_path $MODEL_PATH \
    --beams 1 \
    --max_length 40 \
    --task index_with_sep \
    --device 0
