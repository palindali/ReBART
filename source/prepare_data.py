# Transform data from DC format to ReBART format

import pickle
import json
import numpy as np

# Load pickle
filename = './data/train.pickle'
with open(filename, 'rb') as file:
    train = pickle.load(file)

ld = []
for key, val in train.items():
    story = val[0]
    order = val[1]
    order = order.astype('str').tolist()
    ld.append(
        {"orig_sents" : order,
         "shuf_sents" : story}
    )

with open('./ReBART/data/dc2/train.jsonl', 'w') as outfile:
    for entry in ld:
        json.dump(entry, outfile)
        outfile.write('\n')
