import os
import json

def text_encode(path, file):
    global encode_dict
    global x_train, y_train, x_test, y_test
    global n
    #  print(file)
    if file[0] != '.':
        n += 1
        path = os.path.join(path, file)
        with open(path, 'r') as f:
            text = f.read()
            seg = text.split()
            f.close()

        encode_list = list()

        for voc in seg:
            num = encode_dict[voc]
            if num<20000:
                encode_list.append(num)

            else:
                encode_list.append(0)

        #  encode_text = ' '.join(encode_list)

        if "中央社" in path:
            flag = 1

        else:
            flag = 0

        if n<=10000:
            x_train.append(encode_list)
            y_train.append(flag)

        else:
            x_test.append(encode_list)
            y_test.append(flag)
    
        #  x_path = os.path.join(encode_path, file)
        #
        #  with open(x_path, 'w') as f:
        #      f.write(encode_text)
        #      f.close()

def go_through(path):
    global  encode_path

    allfile = os.listdir(path)

    for item in allfile:
        next_path = os.path.join(path, item)
        #  print(next_path)

        if os.path.isdir(next_path):
            go_through(next_path)

        elif os.path.isfile(next_path):
            text_encode(path, item)

with open("./Encode.json", 'r') as j:
    encode_dict = json.load(j)
    j.close

path = r'./Segmentation'

n = 0

x_path = r'./X/train'
y_path = r'./Y/'

x_train = list()
y_train = list()

x_test = list()
y_test = list()

go_through(path)

