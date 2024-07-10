import json
import os
import random

from keras.layers import LSTM, Dense, Embedding
from keras.models import Sequential, load_model
from keras.preprocessing import sequence


def text_encode(path, file):
    global encode_dict
    global x_train, y_train, x_test, y_test
    global n
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
            if num<max_encode:
                encode_list.append(num)

            else:
                encode_list.append(0)


        if "中央社" in path:
            flag = 1

        else:
            flag = 0

        r = random.randint(1,10)
            
        if r>1:
            x_train.append(encode_list)
            y_train.append(flag)

        else:
            x_test.append(encode_list)
            y_test.append(flag)
    

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

with open("./preprocessing/Encode.json", 'r') as j:
    encode_dict = json.load(j)
    j.close

path = r'./data/segmented-data'

n = 0

x_train = list()
y_train = list()

x_test = list()
y_test = list()

go_through(path)

x_train = sequence.pad_sequences(x_train, maxlen=150)
x_test = sequence.pad_sequences(x_test, maxlen=150)


model = Sequential()
model.add(Embedding(max_encode, 10))
model.add(LSTM(10))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy',
                            optimizer='adam',
                            metrics=['accuracy'])
print(model.summary())
model.fit(x_train, y_train,
                    batch_size=32,
                    epochs=5)
score = model.evaluate(x_test, y_test)
print('loss = {0:.2f}'.format(score[0]))
print('正確率 = {0:.2f}%'.format(score[1]*100))
model.save('my_model.h5')

