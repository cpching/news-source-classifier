import time
import os 
import shutil

def move(path, file):
    if file[0] != '.':
        print(file)
        #  path = os.path.join(path, file)
        #  with open(path, 'r') as f:
        #      text = f.read()
        #      seg = text.split()
        #      f.close()

def go_through(path):
    allfile = os.listdir(path)

    for item in allfile:
        next_path = os.path.join(path, item)
        #  print(next_path)

        if os.path.isdir(next_path):
            go_through(next_path)

        elif os.path.isfile(next_path):
            if os.path.getsize(next_path) < 70:
                move(path, item)
                shutil.move(next_path, '../../Desktop/small')
        
path = r'./Segmentation'

go_through(path)

#  tStart = time.time()#計時開始
#  voc_dir.most_common()
#  tEnd = time.time()#計時結束
#  print("It cost %f sec" % (tEnd - tStart))

#  print(voc_dict)
tStart = time.time()#計時開始
tEnd = time.time()#計時結束
print("It cost %f sec" % (tEnd - tStart))

i = 1

encode_dict = {}

