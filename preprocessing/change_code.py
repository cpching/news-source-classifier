import os

path = './change/'

allfile = os.listdir(path)

for file in allfile:
    print(file)
    with open(path+file, 'rb') as f:
        text = f.read()
        #  print(text)
        f.close()

        text = text.decode('big5')
        print(text)

        f = open(path+file, 'wb')# 開檔
        f.write(text.encode('utf-8'))  # 寫入 unicode 格式
        f.close()          # 關閉檔案

