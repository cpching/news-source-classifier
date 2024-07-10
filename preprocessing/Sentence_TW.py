import os

month = '2019_12'
seg = '01/'

path = r'./中央社/' + month + '/' + seg
des_path = r'./中央社/' + month + '_Sentence/' + seg 

all_file = os.listdir(path)

if not os.path.isdir(des_path):
    os.makedirs(des_path)

for file in all_file:
    print(file)

    if file[0] != '.':
        with open(path+file, 'r') as f:
            text = f.read()
            l = text.split('\n')
            l.pop(0)
            l.pop(0)
            l.pop(0)
            text = '。'.join(l)
            l = text.split('。')
            #print(l)
            text=''
            file = file.split('.')[0]

            for i in range(len(l)):
                text += l[i]+'。'

                if not (i+1)%3:
                    file_name = des_path + file + '_{:0>2s}'.format(str((i+1)//3)) + ".txt"
                    with open(file_name, 'w') as f_s:
                        f_s.write(text)
                        f_s.close()
                    print(file_name)
#                    print(text + '\n')
                    text = ''
                

            f.close()

