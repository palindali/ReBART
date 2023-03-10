# Format the predictions
import json
import pandas as pd
import pdb

# Read output jsonl file
in_file = './outputs/bart-large_dc2/test_bart_greedy.jsonl'
all_lines = []
with open(in_file, "r", encoding="utf-8") as f:
    for line in f:
        all_lines.append(json.loads(line))

# Extract prediction orders
# pdb.set_trace()
orders = [[int(v) for v in line['predictions'][0][:-6].split(' ')] for line in all_lines]

# Save orders dataframe in DC format
orders_df = pd.DataFrame(orders)
orders_df.columns = ['index_1', 'index_2', 'index_3', 'index_4', 'index_5']
orders_df['id'] = range(len(orders_df))
orders_df = orders_df[['id','index_1', 'index_2', 'index_3', 'index_4', 'index_5']]
orders_df.to_csv(in_file[:-6] + "_orders.csv", index=False)
