# Format the predictions
import json

in_file = './outputs/bart-large_dc2/test_bart_greedy.jsonl'
all_lines = []
with open(in_file, "r", encoding="utf-8") as f:
    for line in f:
        all_lines.append(json.loads(line))

orders = [line['predictions'] for line in all_lines]
