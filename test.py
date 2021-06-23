import json
import pickle
import numpy as np
with open('data/notes', 'rb') as filepath:
    notes = pickle.load(filepath)
    pitchnames = sorted(set(item for item in notes))
    # Get all pitch names
    n_vocab = len(set(notes))
    jsonStr = json.dumps(notes)
    # with open("data/notes.json", 'w') as f:
    #     f.writelines(jsonStr)

    print(str(pitchnames))

# x = np.zeros((2, 3, 1))
# print(str(x))

# a = np.arange(6).reshape(2,3)+15
# print(a)
# print(np.argmax(a, 1))
