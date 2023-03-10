# Transform data from DC format to ReBART format

import pickle
import json
import numpy as np

# Load pickle
filename = './data/test_right.pickle'
with open(filename, 'rb') as file:
    test = pickle.load(file)

ld = []
for key, val in test.items():
    story = val
    ld.append(
        {"orig_sents" : [],
         "shuf_sents" : story}
    )
    # break

with open('./ReBART/data/dc2/test.jsonl', 'w') as outfile:
    for entry in ld:
        json.dump(entry, outfile)
        outfile.write('\n')
