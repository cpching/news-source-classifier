from collections import Counter
import time
import os 
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import sequence
import json

f_n = 0


def encode(path, file):
    global voc_dict, f_n
    #  print(file)
    if file[0] != '.':
        f_n += 1
        path = os.path.join(path, file)
        with open(path, 'r') as f:
            text = f.read()
            seg = text.split()
            voc_dict.update(Counter(seg))
            f.close()

def go_through(path):
    allfile = os.listdir(path)

    for item in allfile:
        next_path = os.path.join(path, item)
        #  print(next_path)

        if os.path.isdir(next_path):
            go_through(next_path)

        elif os.path.isfile(next_path):
            encode(path, item)
        
tStart = time.time()#計時開始

path = r'./Segmentation'

voc_dict = Counter()

go_through(path)

encode_path = r'./Encode'

#  tStart = time.time()#計時開始
#  voc_dir.most_common()
#  tEnd = time.time()#計時結束
#  print("It cost %f sec" % (tEnd - tStart))

#  print(voc_dict)
voc_dict = sorted(voc_dict, key=voc_dict.get, reverse=True)

i = 1

encode_dict = {}

for voc in voc_dict:
    encode_dict[voc] = i
    i += 1

encode_text = list()

#  global encode_text
#  with open(path, 'r') as f:
#      text = f.read()
#
#      for voc in text.split():
#          encode_text.append(encode_dict[voc])
#
#      f.close()

#  encode_text = sequence.pad_sequences(encode_text, maxlen=150)

#  print(encode_dict)

jsObj = json.dumps(encode_dict)

with open('./Encode.json', 'w') as fileObject:
    fileObject.write(jsObj)
    fileObject.close()
    fileObject.close()

tEnd = time.time()#計時結束
print("It cost %f sec" % (tEnd - tStart))
print(f_n)
