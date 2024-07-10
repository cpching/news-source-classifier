import os
import re
import string
import time

from ckiptagger import NER, POS, WS

tStart = time.time()#計時開始

path = r'./News/人民日報/2019_12/09/' # /和/之間是放資料來源的路徑 .代表跟這個檔案同一個目錄 相對位置
# ex: ./人民日報/2019_12/ 代表放在人民日報下的2019_12資料夾裡 最後一定要有/
path_seg = r'./Segmentation/人民日報/2019_12/09/' # 放資料存放位置 因為我把最終的檔名取一樣 所以不能跟 path 相同

allfile = os.listdir(path)

text=''

if not os.path.isdir(path_seg):
    os.makedirs(path_seg)

for file in allfile:
    print(file)
    if os.path.isfile(path_seg + file):
        continue

    if file[0] != '.':
        with open(path + file, 'r') as f:
            text = f.read()
            f.close()
            text = text.replace('+', '').replace('-', '').replace('‘', '').replace('’', '').replace('\t', '').replace('\xa0','').replace('\n','').replace(' ','').replace('\u3000','').replace('[^\w\s]','').replace('“',"").replace('”',"").replace('／',"").replace('《','').replace('》','').replace('，','').replace('。','').replace('「','').replace('」','').replace('（','').replace('）','').replace('！','').replace('？','').replace('、','').replace('▲','').replace('…','').replace('：','').replace('；','').replace('—','').replace('●','').replace('■','').replace('【','').replace('】','').replace('(','').replace(')','').replace('〔','').replace('〕','').replace('!','').replace('?','').replace('︹','').replace('︺','')

    ws = WS("./data")
    ws_results = ws([text])
    del ws
    result = ' '.join(ws_results[0])
    
    with open(path_seg + file, 'w') as f:
        f.write(result)
        f.close()

tEnd = time.time()#計時結束
#列印結果
print("It cost %f sec" % (tEnd - tStart))#會自動做進位

