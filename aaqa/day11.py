import jieba
import sys
sys.path.append("../")
import jieba.posseg as pseg
# datas=("李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
#        "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
#        "「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。")
# words = jieba.lcut(datas)
# print("/".join(words))
#
# jieba.load_userdict("dict.txt")
# jieba.add_word("石墨烯")
# words = jieba.lcut(datas)
# print("/".join(words))

# with open("./stopword/hgd.txt",encoding="utf-8") as f:
#     line = f.read()
#     print(line)
# import jieba
# datas = line
# words = jieba.lcut(datas)
# print("/".join(words))
# print("="*50)
#
# jieba.load_userdict("dict.txt")
# words = jieba.lcut(datas)
# print("/".join(words))

# for i in words:
#     print(i)

import torch
from ltp import LTP
ltp=LTP("ltp")
if torch.cuda.is_available():
    print(111)
    ltp.to("cuda")
sents=ltp.pipeline(["我爱北京天安门","他叫汤姆去哪外衣","汤姆生病了"],tasks=["cws","pos","ner","dep"])
print(sents)
print(sents.cws)
print(sents.pos)
print(sents.sdp)