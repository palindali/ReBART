#!/bin/bash


DATA_DIR="data/dc2"
OUT_DIR="outputs/bart-large_dc2"

mkdir -p ${OUT_DIR}
cp $0 ${OUT_DIR}

python -m source.encoder_decoder --train_file data/dc2/train.jsonl --eval_data_file data/dc2/dev.jsonl --out_dir outputs/bart-large_dc2 --model_type facebook/bart-large --model_name_or_path facebook/bart-large --device 1 --do_train --save_total_limit 1 --num_train_epochs 5 --logging_steps 3000 --gradient_accumulation_steps 8 --train_batch_size 4 --eval_batch_size 8 --overwrite_out_dir --max_input_length 1024 --max_output_length 40 --task index_with_sep
# --do_eval \
#--overwrite_cache \
